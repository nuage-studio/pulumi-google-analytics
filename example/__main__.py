import pulumi
from pulumi_google_analytics.dynamic_providers import WebProperty, WebPropertyArgs


config = pulumi.Config()

ga_account_id = config.require("ga_account_id")

# create or fetch web-property
web_property = WebProperty(
    "example-web_property",
    args=WebPropertyArgs(
        account_id=ga_account_id,
        site_name="example.com",
        site_url="https://example.com",
    ),
)

pulumi.export("tracking_id", web_property.tracking_id)