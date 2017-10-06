#! /usr/bin/env python3

import LogsModule

# What are the most popular three articles of all time?
articles_results = LogsModule.Query(
    "What are the most popular three "
    "articles of all time?",
    "select articles.title, count(*) as views "
    "from articles inner join log on log.path "
    "like concat('%', articles.slug, '%') "
    "where log.status like '%200%' group by "
    "articles.title, log.path order by views desc limit 3")

# Who are the most popular article authors of all time?
authors_results = LogsModule.Query(
    "Who are the most popular article authors of all time?",
    "select authors.name, count(*) as views from articles inner "
    "join authors on articles.author = authors.id inner join log "
    "on log.path like concat('%', articles.slug, '%') where "
    "log.status like '%200%' group "
    "by authors.name order by views desc")

# On which days did more than 1% of requests lead to errors?
errors_results = LogsModule.Query(
    "On which days did more than 1% of requests lead to errors?",
    "select day, perc from ("
    "select day, round((sum(requests)/(select count(*) from log where "
    "substring(cast(log.time as text), 0, 11) = day) * 100), 2) as "
    "perc from (select substring(cast(log.time as text), 0, 11) as day, "
    "count(*) as requests from log where status like '%404%' group by day)"
    "as log_percentage group by day order by perc desc) as final_query "
    "where perc >= 1")


if __name__ == '__main__':


    articles_results.get_query_result()
    articles_results.print_query_results()
    authors_results.get_query_result()
    authors_results.print_query_results()
    errors_results.get_query_result()
    errors_results.print_error_results()
