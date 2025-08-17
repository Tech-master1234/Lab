data <- data.frame(
  x1 = c(1:4, 99999, 1, NA, 1, 1, NA), 
  x2 = c(1:5, 1, "NA", 1, 1, "NA"),
  x3 = c(letters[c(1:3)], "x x", "x", "y y y", "x", "a", "a", NA),
  x4 = "", 
  x5 = NA
)
print("Printing Data",quote = FALSE)
print(data)


data <- data.frame(
  col1 = c(1, 2, 3, 4, 99999, 1, 1, 1, 1),
  col2 = c(1, 2, 3, 4, 5, 1, NA, 1, 1),
  col3 = c("a", "b", "c", "x x", "x", "y y y", "a", NA, "a"),
  stringsAsFactors = FALSE
)
print("=====================================",quote = FALSE)
print("Data Before Cleaning",quote = FALSE)
print(data)

clean_data <- na.omit(data)
print("=====================================",quote = FALSE)
print("Cleaned Output",quote = FALSE)
print(clean_data)

