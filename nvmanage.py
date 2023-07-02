from pynvml import *

nvmlInit()

# General info
print("NVIDIA Driver: ", nvmlSystemGetDriverVersion())
print("NVML Version:  ", nvmlSystemGetNVMLVersion())
print("CUDA Version:  ", str(nvmlSystemGetCudaDriverVersion_v2()).replace('0','.')[:-1])

handle = []

# List of events
evts = {256:'nvmlEventMigConfigChange', 
		128:'nvmlEventTypePowerSourceChange',
		16:'nvmlEventTypeClock',
		8:'nvmlEventTypeXidCriticalError',
		4:'nvmlEventTypePState',
		2:'nvmlEventTypeDoubleBitEccError',
		1:'nvmlEventTypeSingleBitEccError'}

clks = {0:'Graphics',
		1:'SM',
		2:'Memory',
		3:'Video enc/dec'}

# List devices and stuff
for i in range(nvmlDeviceGetCount()):
	handle.append(nvmlDeviceGetHandleByIndex(i))
	print("Device", i, ":", nvmlDeviceGetName(handle[i]))
	
	SupEvTypes = nvmlDeviceGetSupportedEventTypes(handle[i])
	print("  Supported events: ")
	for j in evts.keys():
		if SupEvTypes & j == j:
			print("    "+ evts[j])

    print("  Clocks: ")
    for j in clks.keys():
		try:
			print("    " + clks[j] + ": " + str(nvmlDeviceGetClockInfo(handle[i],j)))
		except:
			print("    " + clks[j] + ": N/A")

    try:
		print("  GPU Operation Mode: " + str(nvmlDeviceGetGpuOperationMode(handle[i])))
	except:
		print("  GPU Operation Mode: N/A")




#fts
nvmlShutdown()
