import timer, time

t = timer.Stopwatch()
t.start()

time.sleep(2)
t.split()
time.sleep(60)
t.split()
time.sleep(60)
t.stop()
print(t.getFormattedTotalTime())
print(t.getFormattedSplitTimes())
