web: pip install . -U && new_package-run

deploy_heroku:

runs-on: ubuntu-latest

steps:
- uses: actions/checkout@v2
- uses: akhileshns/heroku-deploy@v3.0.4 # This is the action
    with:
    heroku_api_key: ${{secrets.HEROKU_API_KEY}}
    heroku_app_name: "newapplewagon123" # Must be unique in Heroku
    heroku_email: ${{secrets.HEROKU_EMAIL}}
