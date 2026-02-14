import kagglehub
from kagglehub import KaggleDatasetAdapter

file_path = "student_lifestyle_performance_dataset.csv"   # <-- CHANGE IF DIFFERENT

df = kagglehub.load_dataset(
    KaggleDatasetAdapter.PANDAS,
    "sehaj1104/student-lifestyle-and-academic-performance-dataset",
    file_path,
    pandas_kwargs={"nrows": 1000}
)
numeric_df = df.select_dtypes(include="number")


data = numeric_df["Study_Hours_per_Day"]  # <-- CHANGE TO column
mean = data.mean()
median = data.median()
mode = data.mode()[0] if not data.mode().empty else "No mode"
data_range = data.max() - data.min()
variance = data.var()
std_dev = data.std()

print(f"\n--- Statistics for Study Hours Per Day of Students---")
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
print("Range:", data_range)
print("Variance:", variance)
print("Standard Deviation:", std_dev)

