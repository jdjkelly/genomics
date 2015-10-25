corr <- function(directory, threshold = 0) {
  ## 'directory' is a character vector of length 1 indicating
  ## the location of the CSV files

  ## 'threshold' is a numeric vector of length 1 indicating the
  ## number of completely observed observations (on all
  ## variables) required to compute the correlation between
  ## nitrate and sulfate; the default is 0

  ## Return a numeric vector of correlations
  ## NOTE: Do not round the result!

  mons <- complete(directory)
  mons <- mons[mons$nobs > threshold,]$id

  files <- list.files(directory, full.names=TRUE)
  cors <- c()
  for (i in mons) {
    data <- read.csv(files[i])
    complete <- data[!is.na(data$nitrate) & !is.na(data$sulfate),]
    cors <- c(cors, cor(complete$sulfate, complete$nitrate))
  }
  cors
}
