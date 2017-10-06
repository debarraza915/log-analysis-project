#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2


class Query(object):

    def __init__(self, query_title, query):


        self.query_title = query_title
        self.query = query
        self.query_results = ""
        self.final_results = ""

    # returns query result
    def get_query_result(self):
        db = psycopg2.connect(database="news")
        c = db.cursor()
        c.execute(self.query)
        self.query_results = c.fetchall()
        db.close()
        self.final_results = self.query_results, self.query_title

    # stores query result
    def print_query_results(self):
        print (self.final_results[1])
        for (index, results) in enumerate(self.final_results[0]):
            print (
                '\t',
                index + 1,
                '-',
                results[0],
                '\t - ',
                str(results[1]),
                'views',
                )

    # print formatted output
    def print_error_results(self):
        print (self.final_results[1])
        for results in self.final_results[0]:
            print ('\t', results[0], '-', str(results[1]) + '% errors')
