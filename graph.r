setwd("D:/TanakitInt/Documents/GitHub/email-analysis")

graphPlot = function()
{
    email = read.csv("output/emailProvider.csv")

    count = table(email$email_provider)

    count_sorted = sort(count, decreasing = TRUE)

    color = c('#8570ca', '#dc2453', '#68b122', '#a0a9f5', 
              '#bb6754', '#148bbb', '#ad106a', '#c8b120', 
              '#c249ef', '#2d5779', '#2ff1b8', '#c49c3c',
              '#e37c8e', '#a61a99', '#c647fa', '#8e45f6', 
              '#d5ce24')

    pie(count_sorted, main = "Count of Email users", col = color)
}
