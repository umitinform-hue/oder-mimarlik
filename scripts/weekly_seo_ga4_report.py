import json
import os
from datetime import date, timedelta
from pathlib import Path

from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import DateRange, Dimension, Metric, RunReportRequest
from google.oauth2 import service_account
from googleapiclient.discovery import build

LANDING_URL = os.environ['LANDING_URL']
SITE_URL = os.environ['GSC_SITE_URL']
PROPERTY_ID = os.environ['GA4_PROPERTY_ID']
SERVICE_ACCOUNT_JSON = os.environ['GOOGLE_SERVICE_ACCOUNT_JSON']

creds_info = json.loads(SERVICE_ACCOUNT_JSON)
scopes = [
    'https://www.googleapis.com/auth/analytics.readonly',
    'https://www.googleapis.com/auth/webmasters.readonly',
]
credentials = service_account.Credentials.from_service_account_info(creds_info, scopes=scopes)

end = date.today()
start = end - timedelta(days=7)
period = {'startDate': start.isoformat(), 'endDate': end.isoformat()}


def ga4_report(dimensions, metrics, dimension_filter=None, limit=25):
    client = BetaAnalyticsDataClient(credentials=credentials)
    request = RunReportRequest(
        property=f'properties/{PROPERTY_ID}',
        dimensions=[Dimension(name=x) for x in dimensions],
        metrics=[Metric(name=x) for x in metrics],
        date_ranges=[DateRange(**period)],
        limit=limit,
    )
    if dimension_filter:
        request.dimension_filter = dimension_filter
    return client.run_report(request)


def rows(report):
    output = []
    for row in report.rows:
        output.append({
            'dimensions': [x.value for x in row.dimension_values],
            'metrics': [x.value for x in row.metric_values],
        })
    return output


def gsc_report():
    service = build('searchconsole', 'v1', credentials=credentials, cache_discovery=False)
    body = {
        'startDate': (end - timedelta(days=28)).isoformat(),
        'endDate': end.isoformat(),
        'dimensions': ['query'],
        'dimensionFilterGroups': [{
            'filters': [{'dimension': 'page', 'operator': 'equals', 'expression': LANDING_URL}]
        }],
        'rowLimit': 25,
    }
    return service.searchanalytics().query(siteUrl=SITE_URL, body=body).execute().get('rows', [])


def main():
    landing = ga4_report(['pagePath'], ['activeUsers', 'sessions', 'screenPageViews'], limit=50)
    sources = ga4_report(['sessionSourceMedium'], ['activeUsers', 'sessions'], limit=25)
    events = ga4_report(['eventName'], ['eventCount'], limit=100)
    queries = gsc_report()

    lines = [
        f'# Öder Mimarlık haftalık SEO + GA4 raporu',
        f'\nDönem: {period["startDate"]} → {period["endDate"]}',
        f'\nLanding: {LANDING_URL}',
        '\n## GA4 landing akışı\n',
    ]
    for r in rows(landing): lines.append(f'- {r["dimensions"]}: {r["metrics"]}')
    lines.append('\n## GA4 kaynak / medium\n')
    for r in rows(sources): lines.append(f'- {r["dimensions"]}: {r["metrics"]}')
    lines.append('\n## GA4 olayları\n')
    for r in rows(events):
        if r['dimensions'][0] in {'oder_generate_lead', 'oder_whatsapp_click', 'oder_hero_lead', 'oder_form_validation_error'}:
            lines.append(f'- {r["dimensions"]}: {r["metrics"]}')
    lines.append('\n## Search Console sorguları\n')
    for r in queries:
        lines.append(f'- {r.get("keys", [])}: clicks={r.get("clicks", 0)}, impressions={r.get("impressions", 0)}, ctr={r.get("ctr", 0):.4f}, position={r.get("position", 0):.2f}')
    lines.append('\n## Not\n')
    lines.append('- Test/QA kampanyaları ayrıca filtrelenmelidir; bu script gerçek müşteri trafiği iddiasında bulunmaz.')
    Path('reports').mkdir(exist_ok=True)
    Path('reports/weekly-seo-ga4-report.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
