server_ph = 0.51
server_pd = server_ph * 24
server_pm = server_pd * 30

print("The server cost is £%s " % (server_ph) + "per hour")
print("The server cost is £%s " % (server_pd) + "per day")
print("The server cost is £%s " % (server_pm) + "per month")


server_pd_20 = server_pd * 20
print("Twenty servers per day would cost %s " % (server_pd_20))
server_pm_20 = server_pd_20 * 30
print("Twenty servers per month would cost %s " % (server_pm_20))

total = 918
server_days = 918 / (server_pd)
print("Maximum day to run one server on budget of £918 would be £%s " % (server_days))
