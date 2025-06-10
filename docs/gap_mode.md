# Gap publishing mode

The default behaviour ("auto" mode) is to publish records for the previous month, and up to the current day of the current month.
If `PUBLISHING_MODE` is set to "gap" instead, then a fixed time period will be queried,
and the start and end of that period must be specified via `QUERY_START` and `QUERY_END` respectively.
The purpose of this is typically to republish records for a period of time when the auto mode was not running correctly.
These times must be in ISO 8601 format to avoid complications with time zones and leap seconds.
The timezone should be specified, and it should be UTC for consistency with the auto publishing mode.

Note: In the case of APEL, since only APEL summary records are supported (not individual job records),
if you specify `QUERY_START` as a time that is not precisely the beginning of a month,
a partial month summary record will be produced and published.
The APEL server may ignore it if it already has a more complete summary record for that month containing more jobs.
Therefore when using gap mode, you should most likely make sure that `QUERY_START` is precisely the beginning of a month
in order to produce a complete summary record for that month which will take precedence over
any other records containing fewer jobs that may have already been published.
The same applies for `QUERY_END` matching the end of the month (unless it is the current month at the time of publishing,
in which case a subsequent run in auto mode will eventually complete the records for this month).
So, `QUERY_START` (and possibly `QUERY_END`) should each look like e.g. 'YYYY-MM-01T00:00:00+00:00'
for a given year "YYYY" and month "MM".

# Validation

The typical use of gap mode is to publish records for a fixed past time period,
in which case the results should be deterministic and reproducible.
For that reason, gap mode is also useful for validating consistency when changes are made in the Kuantifier code, or monitoring stack.
