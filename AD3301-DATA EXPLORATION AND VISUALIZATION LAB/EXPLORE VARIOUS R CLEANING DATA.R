data <- data.frame(
  x1 = c(1:4, 99999, 1, NA, 1, 1, NA), 
  x2 = c(1:5, 1, "NA", 1, 1, "NA"),
  x3 = c(letters[c(1:3)], "x x", "x", "y y y", "x", "a", "a", NA),
  x4 = "", 
  x5 = NA
)
print(data)
data <- na.omit(data)
print(data)
