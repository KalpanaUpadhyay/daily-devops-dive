# Change Log

## v1.24.1 - 2025-04-03

- 🐛 **Fix**: Fix handling filters for aggregate queries

## v1.24.0 - 2025-04-01

- 🐛 **Fix**: improvements to connection management

## v1.23.3 - 2025-03-21

- ⚙️ **Chore**: Improve configuration page

## v1.23.2 - 2025-03-18

- 🐛 **Fix**: Support dot notation object paths in the adhoc filters

## v1.23.1 - 2025-03-17

⚙️ **Chore**: Create logger from context

## v1.23.0 - 2025-03-11

- 🐛 **Fix**: Fix ad hoc filters implementation

## v1.22.18 - 2025-03-11

- ⚙️ **Chore**: Improve logging

## v1.22.17 - 2025-03-04

- 🐛 **Fix**: Fix connection issues

## v1.22.16 - 2025-02-28

- ⚙️ **Chore**: Fix logging

## v1.22.15 - 2025-02-20

- ⚙️ **Chore**: Improve logging

## v1.22.14 - 2025-02-19

- ⚙️ **Chore**: Improve error handling

## v1.22.13 - 2025-02-17

- ⚙️ **Chore**: Improve error logging

## v1.22.12 - 2025-02-12

- ⚙️ **Chore**: Improve logging

## v1.22.11 - 2025-02-11

- ⚙️ **Chore**: Improve error tracking

## v1.22.10 - 2025-02-11

- ⚙️ **Chore**: Update backend dependencies

## v1.22.9 - 2025-02-04

- ⚙️ **Chore**: Update frontend dependencies

## v1.22.8 - 2025-01-10

- ⚙️ **Chore**: Update backend dependencies

## v1.22.7 - 2024-12-18

- ⚙️ **Chore**: Update backend dependencies

## v1.22.6 - 2024-12-16

- ⚙️ **Chore**: Update backend dependencies

## v1.22.5 - 2024-12-11

- 🐛 **Fix**: Fix connection issue

## v1.22.4 - 2024-12-03

- ⚙️ **Chore**: Update dependencies

## v1.22.3 - 2024-11-27

- 🐛 **Fix**: Fix potential null accesses

## v1.22.2 - 2024-11-21

- ⚙️ **Chore**: Remove error source http client and replace with methods

## v1.22.1 - 2024-11-12

- ⚙️ **Chore**: Updated backend dependencies

## v1.22.0 - 2024-10-24

- 🐛 **Fix**: Ensure we disconnect client on ds disposal

## v1.21.0 - 2024-10-23

- 🐛 **Fix**: Fixes support for timestamps in query via Date.now and basic arithmetic only on timestamps

## v1.20.0 - 2024-10-18

- 🐛 **Fix**: Add support for Date.now() timestamps in queries

## v1.19.4 - 2024-10-03

- ⚙️ **Chore**: Update frontend dependencies
- ⚙️ **Chore**: Minimal supported Grafana version is now `10.4.8`

## v1.19.3 - 2024-10-02

- ⚙️ **Chore**: update backend dependencies

## v1.19.2 - 2024-09-23

- ⚙️ **Chore**: Update backend dependencies

## v1.19.1 - 2024-08-30

- ⚙️ **Chore**: update backend dependencies

## v1.19.0 - 2024-07-16

- ⚙️ **Chore**: Capture error source

## v1.18.0 - 2024-07-09

- 🐛 **Fix**: Moves / Fixes Date parsing by moving to backend

## v1.17.0 - 2024-07-05

- ⚙️ **Chore**: Added SLO metrics to the plugin

## v1.16.0 - 2024-06-18

- ⚙️ **Chore**: adding custom TLS config for encrypted TLS Certificates

## v1.15.0 - 2024-06-10

- 🐛 **Fix**: move evaluation of Date() to mongodb server

## v1.14.2 - 2024-06-07

- 🐛 **Fix**: update license check logic

## v1.14.1 - 2024-06-05

- ⚙️ **Chore**: Update backend dependencies

## v1.14.0 - 2024-06-03

- ⚙️ **Chore**: Update backend dependencies

## v1.13.0 - 2024-05-28

- 🐛 **Fix**: Update client to handle authMechanismProperties correctly

## v1.12.1 - 2024-04-05

- 🚀 **Feature**: Add support for krb5 configuration

## v1.12.0 - 2024-03-15

- 🐛 **Fix**: Include kerberos libkrb5-dev in .zip

## v1.11.6 - 2024-03-13

- ⚙️ **Chore**: Backend binaries are now compiled with Go version `1.22.1`

## v1.11.5 - 2024-03-05

- ⚙️ **Chore**: Update dependencies

## v1.11.4 - 2024-02-14

- 🐛 **Fix**: tweaks loading old basic auth settings from versions older than 1.9.0

## v1.11.3 - 2024-01-29

- ⚙️ **Chore**: Allow 9.4.7

## v1.11.2 - 2024-01-22

- 🐛 **Fix**: better onRunQuery function for better grafana version compatibility

## v1.11.1 - 2024-01-22

- 🐛 **Fix**: fix for variable query editor run query button

## v1.11.0 - 2024-01-17

- 🚀 **Feature**: Add Kerberos support

## v1.10.3 - 2023-12-08

- 🐛 **Fix**: url encode special characters on connection string

## v1.10.2 - 2023-11-30

- ⚙️ **Chore**: update sdk version to capture plugin error source

## v1.10.1 - 2023-11-29

- ⚙️ **Chore**: update mongodb driver to latest version (1.13.0)

## v1.10.0 - 2023-11-14

- ⚙️ **Chore**: update dependencies to latest versions
- ⚙️ **Chore**: Update minimal required grafana version to 9.5.13

## v1.9.7 - 2023-10-27

- 📝 **Documentation**: Updated the MongoDB data source documentation

## v1.9.6 - 2023-10-10

- 🐛 **Fix**: fixes an issue extracting the database name from the connection string

## v1.9.5 - 2023-10-09

- ⚙️ **Chore**: compiled using mongodb official go driver v1.11.9 which fixes some connection issues

## v1.9.4 - 2023-09-27

- ⚙️ **Chore**: migrate from grafana toolkit to @grafana/create-plugin for frontend bundle tooling

## v1.9.3 - 2023-09-18

- 🐛 **Fix**: Fix health check message

## v1.9.2 - 2023-08-23

- 🐛 **Fix**: adds a rows limit option to prevent plugin from crashing on larger queries. also adds better logging to debug performance

## v1.9.1 - 2023-08-22

- ⚙️ **Chore**: backend libs updated with golang:1.21

## v1.9.0 - 2023-07-21

- ⚙️ **Chore**: Revamp the Config UI with new components

## v1.8.3 - 2023-06-08

- ⚙️ **Chore**: backend libs updated with golang:1.20.5

## v1.8.2 - 2023-05-11

- 🐛 **Fix**: skip diagnostic commands when parsing the query

## v1.8.1 - 2023-05-10

- 🐛 **Fix**: Updated UI to ensure additional settings label width are consistent

## v1.8.0 - 2023-05-10

- 🚀 **Feature**: [Secure socks proxy](https://grafana.com/docs/grafana/next/setup-grafana/configure-grafana/proxy/) support added

## v1.7.4 - 2023-05-04

- ⚙️ **Chore**: Backend binaries are now compiled with `golang:1.20.4`

## v1.7.3 - 2023-04-19

- ⚙️ **Chore**: Backend binaries are now compiled with `golang:1.20.3`

## v1.7.2 - 2023-04-10

- 🐛 **Fix**: Parser - format multi values as strings

## v1.7.1 - 2023-03-28

- 🐛 **Fix**: Parse queries properly that contain double $$ like "$$ROOT"

## v1.7.0 - 2023-03-27

- 🚀 **Feature**: Query Editor - Expand/collapse, Syntax Highlighting, Syntax Validation, Run button
- 🚀 **Feature**: Config Editor - UI/UX improvements
- ⚙️ **Chore**: Cleanup docs

## v1.6.2 - 2023-03-21

- 🐛 **Fix**: Revert toolkit removal - parser failing

## v1.6.1 - 2023-03-20

- 🐛 **Fix**: Repeating panels with compound variables

## v1.6.0 - 2023-03-20

- 🚀 **Feature**: Support Alerting with Wide Frames for Time Series data

## v1.5.1 - 2023-02-03

- ⚙️ **Chore**: Update frontend dependencies

## v1.5.0 - 2023-01-25

- 🚀 **Feature**: Updated UI layout, tooltips and error messages

## v1.4.12 - 2022-12-16

- ⚙️ **Chore**: Updated backend grafana dependencies
- ⚙️ **Chore**: Backend compiled with the latest version of go (1.19.4)

## v1.4.11 - 2022-11-10

- 🐛 **Fix**: check for faceted results
- ⚙️ **Chore**: go version 1.19

## v1.4.10 - 2022-11-01

- 🐛 **Fix**: parser when using compound variables
- 🐛 **Fix**: interpolation when selecting a template variable

## v1.4.9 - 2022-10-17

- 🐛 **Fix**: parser when using macros

## v1.4.8 - 2022-10-07

- 🐛 **Fix**: parser when using find with projections

## v1.4.7 - 2022-10-04

- 🐛 **Fix**: remove carriage return (`\r`) characters when parsing multi-line aggregate queries

## v1.4.6 - 2022-10-03

- 🐛 **Fix**: Fixed an issue where space around find/aggregate queries were failing
- 🐛 **Fix**: Fixed an issue where `$__timeFrom` and `$__timeTo` macros interpolated incorrectly in variable queries
- 🐛 **Fix**: Fixed an issue where hide query doesn't work as expected

## v1.4.5 - 2022-09-19

- 🐛 **Fix**: issue with numeric template variables

## v1.4.3 - 2022-09-14

- 🐛 **Fix**: remove carriage return (`\r`) characters in multi-line aggregate queries

## v1.4.2 - 2022-09-06

- Query inspector in grafana now shows the executed query
- 🐛 **Fix**: `$__timeFrom`/`$__timeTo` macros not working properly
- ⚙️ **Chore**: Updated docs with more examples

## v1.4.1 - 2022-08-08

- 🐛 **Fix**: queries were not in the query editor after saving

## v1.4.0 - 2022-06-07

- 🚀 **Feature**: Add support for ObjectId, regex patterns and single-quote usage

## v1.3.0 - 2022-03-31

- 🐛 **Fix**: handle numeric values always as floats

## v1.2.1 - 2022-03-24

- ⚙️ **Chore**: Fix docs \$\_\_timeTo macro

## v1.2.0 - 2022-03-15

- 🚀 **Feature**: Update driver to support serverless and MongoDB 5.x features

## v1.1.12 - 2022-01-19

- 🐛 **Fix**: Textbox variables apply properly

## v1.1.11 - 2022-01-19

- 🐛 **Fix**: Compound variables with newer Grafana versions
- 🐛 **Fix**: ISODate when using aggregate function

## v1.1.10 - 2022-01-07

- ⚙️ **Chore**: License, Update SDK

## v1.1.9 - 2021-10-29

- 🐛 **Fix**: Handle collections containing dots

## v1.1.7 - 2021-05-20

- 🚀 **Feature**: Allow injecting template variables into other template variables

## v1.1.6 - 2021-04-28

- 🐛 **Fix**: Handle nullable Boolean values

## v1.1.5 - 2021-04-09

- ⚙️ **Chore**: update enterprise and plugin sdk

## v1.1.4 - 2021-02-06

- 🚀 **Feature**: Time Series grouping by \_\_metric
- 🚀 **Feature**: Convert Interval variables to ms with \_ms suffix

## v1.1.1 - 2021-01-25

- **Workaround** - Build with Go 1.14.14 to workaround old common name certs

## v1.1.0 - 2021-01-19

- 🚀 **Feature**: TLS/SSL support

## v1.0.3 - 2021-01-08

- 🐛 **Fix**: Time Macros in Aggregation #46

## v1.0.2 - 2020-10-28

- 🐛 **Fix**: Signing issue

## v1.0.1 - 2020-10-23

- 🐛 **Fix**: Readme badge/links

## v1.0.0 - 2020-10-23

- Initial release
