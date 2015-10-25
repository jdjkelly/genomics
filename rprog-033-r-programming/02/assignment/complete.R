complete <- function(directory, id = 1:332) {
  ## 'directory' is a character vector of length 1 indicating
  ## the location of the CSV files

  ## 'id' is an integer vector indicating the monitor ID numbers
  ## to be used
  
  ## Return a data frame of the form:
  ## id nobs
  ## 1  117
  ## 2  1041
  ## ...
  ## where 'id' is the monitor ID number and 'nobs' is the
  ## number of complete cases
  files <- dir(directory)
  sums <- numeric()
  for (i in id) {
    data <- read.csv(file.path(directory, files[i]))
    sums <- c(sums, sum(!is.na(data$nitrate) & !is.na(data$sulfate)))
  }
  data.frame(id = id, nobs = sums)
}
