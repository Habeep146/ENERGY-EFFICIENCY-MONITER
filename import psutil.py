import psutil
import time
import matplotlib.pyplot as plt

def get_energy_metrics():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    return cpu_usage, memory_usage

cpu_data = []
memory_data = []
timestamps = []

print("Monitoring energy efficiency... Press Ctrl+C to stop.")

try:
    for i in range(10):  # Simulate for 10 intervals
        cpu, memory = get_energy_metrics()
        timestamp = time.strftime("%H:%M:%S")
        cpu_data.append(cpu)
        memory_data.append(memory)
        timestamps.append(timestamp)
        print(f"[{timestamp}] CPU: {cpu}%, Memory: {memory}%")
        time.sleep(1)
except KeyboardInterrupt:
    print("Monitoring stopped.")

plt.figure(figsize=(10, 5))
plt.plot(timestamps, cpu_data, label='CPU Usage (%)', marker='o')
plt.plot(timestamps, memory_data, label='Memory Usage (%)', marker='x')
plt.xlabel('Time')
plt.ylabel('Usage (%)')
plt.title('Energy Efficiency Monitor')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
