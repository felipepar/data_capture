from data_capture import DataCapture

capture = DataCapture()
capture.add(3)
capture.add(9)
capture.add(3)
capture.add(4)
capture.add(6)
stats = capture.build_stats()


print(f"List to be analyzed: {list(capture.storage.keys())}")
print(f"less than 4: {stats.less(4)}")
print(f"between 3 and 6: {stats.between(3, 6)}")
print(f"greater than 4: {stats.greater(4)}")

