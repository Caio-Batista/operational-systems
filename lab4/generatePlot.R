

mydata4 = read.csv("saidalab4.txt")
png('plot_lab4.png')

attach(mydata4)
par(mfrow=c(2,2))

boxplot(Runtime~Politica,data=mydata4, main="Politica X Runtime", 
        xlab="Politica", ylab="Runtime")
boxplot(Switches~Politica,data=mydata4, main="Politica X Switches", 
        xlab="Politica", ylab="Switches")
boxplot(Average.delay~Politica,data=mydata4, main="Politica X Average delay", 
        xlab="Politica", ylab="Average delay")
boxplot(Wall.clock.time~Politica,data=mydata4, main="Politica X Wall clock time s", 
        xlab="Politica", ylab="Wall clock time")

dev.off()


