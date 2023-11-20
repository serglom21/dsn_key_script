## DSN KEY SCRIPT

The goal of this script is to be used to programmatically set a default rate limit to all project keys in a Sentry.io organization

### How to use it
1. Create an `.env` file with the following  variables:
-  `AUTH_TOKEN` -> Token with `project:admin` and `org:admin` permissions
- `ORG_SLUG`
- `RATELIMIT_WINDOW` -> Time window which is used by rate limit (in seconds - e.g 1 day has 86400 seconds)
- `RATELIMIT_COUNT`

2. Run `bash install.sh` (If it is being run for the first time)
3. Run `bash run.sh` 