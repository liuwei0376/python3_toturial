# -*- coding:utf-8 -*-

import sys


class JobDesc:
    def __init__(self, start_time, end_time, duration, flag):
        self.start_time = start_time
        self.end_time = end_time
        self.duration = duration
        self.flag = flag
    def __str__(self):
        return self.duration + "," + self.flag

def parse_job_desc(desc_data):
    jobname_2_Desc = {}
    ss = desc_data.split("\n")
    for s in ss:
        ss0 = s.strip("\r").split("\t")
        # print(ss0)
        if len(ss0) >= 8:
            print(ss0)
            # jobname_2_Desc[ss0[0]] = JobDesc(get_simple_time(ss0[2]), get_simple_time(ss0[3]), ss0[4], ss0[5])
    return jobname_2_Desc


def statistic(yesterday_data, todayData):
    yesterday_jobs = parse_job_desc(yesterday_data)
    today_jobs = parse_job_desc(todayData)
    # print(yesterday_jobs)
    # print(today_jobs)
    # (success_jobs, failed_jobs, missed_jobs) = gen_statistic(yesterday_jobs, today_jobs)
    # body = html % ( fill_fail_content(failed_jobs), fill_miss_content(missed_jobs), fill_success_content(success_jobs))
    # print(body)


if __name__ == '__main__':
    yesterday_data = sys.argv[1]
    today_data = sys.argv[2]
    statistic(yesterday_data, today_data)
