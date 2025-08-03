import pandas as pd
import numpy as np

schools = pd.read_csv("schools.csv")

best_math_schools = schools[["school_name", "average_math"]][schools["average_math"] >= 0.8*800].sort_values("average_math", ascending=False)

schools["total_SAT"] = schools["average_math"] + schools["average_reading"] + schools["average_writing"]
top_10_schools = schools[["school_name", "total_SAT"]].sort_values("total_SAT", ascending=False).head(10)

borough_std = schools.groupby("borough")["total_SAT"].std()
borough = borough_std.idxmax()
schools_borough = schools[schools["borough"] == borough]
num_schools = schools_borough["school_name"].count()
average_SAT = np.round(schools_borough["total_SAT"].mean(), 2)
std_SAT = np.round(schools_borough["total_SAT"].std(), 2)
largest_std_dev = pd.DataFrame([[borough, num_schools, average_SAT,std_SAT]])
largest_std_dev.columns = ["borough", "num_schools", "average_SAT", "std_SAT"]


