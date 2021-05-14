def regex():
    _regex = {
        'google_api': r'AIza[0-9A-Za-z-_]{35}',
        'firebase'  : r'AAAA[A-Za-z0-9_-]{7}:[A-Za-z0-9_-]{140}',
        'google_captcha' : r'6L[0-9A-Za-z-_]{38}|^6[0-9a-zA-Z_-]{39}$',
        'google_oauth'   : r'ya29\.[0-9A-Za-z\-_]+',
        'amazon_aws_access_key_id' : r'AKIA[0-9A-Z]{16}',
        'amazon_mws_auth_toke' : r'amzn\\.mws\\.[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}',
        'amazon_aws_url' : r's3\.amazonaws.com[/]+|[a-zA-Z0-9_-]*\.s3\.amazonaws.com',
        'amazon_aws_url2' : r"(" \
               r"[a-zA-Z0-9-\.\_]+\.s3\.amazonaws\.com" \
               r"|s3://[a-zA-Z0-9-\.\_]+" \
               r"|s3-[a-zA-Z0-9-\.\_\/]+" \
               r"|s3.amazonaws.com/[a-zA-Z0-9-\.\_]+" \
               r"|s3.console.aws.amazon.com/s3/buckets/[a-zA-Z0-9-\.\_]+)",
        'facebook_access_token' : r'EAACEdEose0cBA[0-9A-Za-z]+',
        'facebook_AppSecret': r"https://graph.facebook.com(:[0-9]+)?/([a-zA-Z0-9_-]+/?)+\?(client_secret=[a-zA-Z0-9]{32}|&|client_id=[0-9]+)+",
        'authorization_basic' : r'basic [a-zA-Z0-9=:_\+\/-]{5,100}',
        'authorization_bearer' : r'bearer [a-zA-Z0-9_\-\.=:_\+\/]{5,100}',
        'authorization_api' : r'api[key|_key|\s+]+[a-zA-Z0-9_\-]{5,100}',
        'mailgun_api_key' : r'key-[0-9a-zA-Z]{32}',
        'twilio_api_key' : r'SK[0-9a-fA-F]{32}',
        'twilio_account_sid' : r'AC[a-zA-Z0-9_\-]{32}',
        'twilio_app_sid' : r'AP[a-zA-Z0-9_\-]{32}',
        'paypal_braintree_access_token' : r'access_token\$production\$[0-9a-z]{16}\$[0-9a-f]{32}',
        'square_oauth_secret' : r'sq0csp-[ 0-9A-Za-z\-_]{43}|sq0[a-z]{3}-[0-9A-Za-z\-_]{22,43}',
        'square_access_token' : r'sqOatp-[0-9A-Za-z\-_]{22}|EAAA[a-zA-Z0-9]{60}',
        'stripe_standard_api' : r'sk_live_[0-9a-zA-Z]{24}',
        'stripe_restricted_api' : r'rk_live_[0-9a-zA-Z]{24}',
        'github_access_token' : r'[a-zA-Z0-9_-]*:[a-zA-Z0-9_\-]+@github\.com*',
        "github_token" : r'ghp_[a-zA-Z0-9]{36}',
        'rsa_private_key' : r'-----BEGIN RSA PRIVATE KEY-----',
        'ssh_dsa_private_key' : r'-----BEGIN DSA PRIVATE KEY-----',
        'ssh_dc_private_key' : r'-----BEGIN EC PRIVATE KEY-----',
        'pgp_private_block' : r'-----BEGIN PGP PRIVATE KEY BLOCK-----',
        'json_web_token' : r'ey[A-Za-z0-9-_=]+\.[A-Za-z0-9-_=]+\.?[A-Za-z0-9-_.+/=]*$',
        'slack_token' : r"("\
               r"(xox[a-zA-Z]-[a-zA-Z0-9-]+)" \
               r"|https://hooks.slack.com/services/([A-Z0-9]+)/([A-Z0-9]+)/([A-Za-z0-9]+))",
        'SSH_privKey' : r"([-]+BEGIN [^\s]+ PRIVATE KEY[-]+[\s]*[^-]*[-]+END [^\s]+ PRIVATE KEY[-]+)",
        'Heroku API KEY' : r'[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}',
        'possible_Creds' : r"(?i)(" \
                        r"password\s*[`=:\"]+\s*[^\s]+|" \
                        r"password is\s*[`=:\"]*\s*[^\s]+|" \
                        r"pwd\s*[`=:\"]*\s*[^\s]+|" \
                        r"passwd\s*[`=:\"]+\s*[^\s]+)",
        'saucelabs' : r"("\
               r"[a-z0-9]{8}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{12}" \
               r"|https?://([a-zA-Z0-9_-](\.)?)+:[a-z0-9]{8}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{12}@ondemand\.[a-zA-Z0-9-]+\.saucelabs\.com(:?([0-9]+))?)",
        'sandgrid' : r"SG\.[a-zA-Z0-9\._-]{22}\.[a-zA-Z0-9\._-]{43}",
        'dropbox' : r"sl\.Aw[a-zA-Z0-9_-]{133}",
        'newrelic_user' : r'NRAK-[A-Z0-9]{27}',
        'newrelic_ingest_license' : r'[a-z0-9]{32}FFFFNRAL',
        'newrelic_ingest_browser' : r'NRBR-[a-z0-9]{19}',
        'asana_token' : r'1/([0-9]{16}):([a-z0-9]{32})',
        'mailchimp_token' : r'[0-9a-f]{32}-us[0-9]{1,2}',
        'wakatime_token' : r'sec_([a-zA-Z0-9]{80})',
        'Foursquare_token' : r'R_[0-9a-f]{32}',
        'Picatic_token' : r'sk_live_[0-9a-z]{32}',
        'ams_token' : r'amzn.mws]{8}-[0-9a-f]{4}-10-9a-f1{4}-[0-9a,]{4}-[0-9a-f]{12}'
    }
    return _regex
