best <- function(state, outcome) {
  # Validate outcome parameter
  if (!(outcome %in% c('heart attack', 'heart failure', 'pneumonia'))) stop('invalid outcome')
  # Assign col value for outcome
  outcome <- switch(outcome, 'heart attack'=11, 'heart failure'=17, 'pneumonia'=23)
  # Load data
  data <- read.csv('outcome-of-care-measures.csv', colClasses = 'character')
  # Validate state param
  if (!(state %in% unique(data$State))) stop('invalid state')
  # Cast outcome col to numeric
  data[,outcome] <- as.numeric(data[,outcome])
  # Create a subset data.frame of c(outcome, hospital name), filtered by the desired state
  data <- subset(data[,c(outcome, 2)], data$State == state & !is.na(data[,outcome]))
  # Find values and return the hospital name
  data[order(data[,1], data$Hospital.Name),][1,]$Hospital.Name
}
