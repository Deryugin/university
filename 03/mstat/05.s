data <- read.table(header=TRUE, con <- textConnection("
subject pre     post
1	9.2	6.7
2	8.7	7
3	5.9	4
4	6	4.2
5	6.5	3.9
6	8.9	5.2
7	7.8	4.5
8	8.1	5.7
9	7.4	3.2
10	6.8	3
"))

t.test(data$pre, data$post, paired=TRUE)
