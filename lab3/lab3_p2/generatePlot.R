

mydata4 = read.csv("exec.csv")
png('plot_lab3_p2.png')

attach(mydata4)
par(mfrow=c(2,2))

boxplot(Runtime~Instancia,data=mydata4, main="Instancia X Runtime", 
        xlab="Instancia", ylab="Runtime")
boxplot(Switches~Instancia,data=mydata4, main="Instancia X Switches", 
        xlab="Instancia", ylab="Switches")
boxplot(Average.delay~Instancia,data=mydata4, main="Instancia X Average delay", 
        xlab="Instancia", ylab="Average delay")
boxplot(Wall.clock.time~Instancia,data=mydata4, main="Instancia X Wall clock time s", 
        xlab="Instancia", ylab="Wall clock time")

dev.off()


