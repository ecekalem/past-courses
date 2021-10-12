setwd('/home/ece')
atomMatrix = as.matrix(read.csv('atomMatrix.csv', header = F))
image(atomMatrix)

atomMatrix[atomMatrix != 0 ] = 1
atomMatrix <- atomMatrix[44:269, 44:269]

## shifting axes
resLabels = c(44,seq(50,260, 10), 269)
atLabels = c((resLabels-43) / (269-43))


image(atomMatrix, useRaster = T, axes=F, xlab = "Residue #", ylab="Residue #")

axis(side=1, at=atLabels, labels = resLabels, las=2)
axis(side=2, at=atLabels, labels = resLabels, las=2)

atomMatrix_contact = atomMatrix
colnames(atomMatrix_contact) = gsub("V", "", colnames(atomMatrix_contact))
rownames(atomMatrix_contact) = colnames(atomMatrix_contact)
for(i in 1:nrow(atomMatrix_contact)){
  for(j in 1:ncol(atomMatrix_contact)){
    if(abs(i-j) == 1){
      atomMatrix_contact[i,j] = 0
    }
  }
}

contactNo <- apply(atomMatrix_contact, 1, function(x) sum(x == 1))
# table(contactNo)
# sort(contactNo, decreasing = T)

image(atomMatrix_contact, useRaster = T, axes=F, xlab = "Residue #", ylab="Residue #")

axis(side=1, at=atLabels, labels = resLabels, las=2)
axis(side=2, at=atLabels, labels = resLabels, las=2)

contactNo <- as.data.frame(contactNo)
contactNo$resNo <- colnames(atomMatrix_contact)
contactNo

contactNo= contactNo[order(contactNo$contactNo),]
contactNo

rmsdList = read.csv('rmsdList.csv', header = F)
rmsdList = rmsdList$V1[2:10]
plot(2:10,rmsdList, xlab = 'Models', ylab = 'RMSD', col = 'black', pch = 19, main = 'Models vs RMSD of 6u3r')
modelno = 2:10
abline(lm(rmsdList ~ (modelno)), col = 'darkblue', lty = 2)


sd(rmsdList)



rsaTable <- read.table('/home/ece/Desktop/rsavalues.txt', header = T, row.names = NULL)
colnames(rsaTable)[1:2] = c("resName", "resNo") 

rsaTable$coordNo = contactNo[as.character(rsaTable$resNo), 1]

plot(rsaTable$coordNo, rsaTable$Ratio, pch = 19, col = 'black',
     xlab = "Coordination number",
     ylab = "Relative ASA")
abline(lm(rsaTable$Ratio ~ rsaTable$coordNo))
cor.test(rsaTable$Ratio, rsaTable$coordNo)
## 	Pearson's product-moment correlation
##
## data:  rsaTable$Ratio and rsaTable$coordNo
## t = -12.023, df = 224, p-value < 2.2e-16
## alternative hypothesis: true correlation is not equal to 0
## 95 percent confidence interval:
##   -0.6995850 -0.5398823
## sample estimates:
##   cor 
## -0.6262597

rsaTable$isCore = sapply(rsaTable$Ratio, function(x){
  ifelse(x <= 5, 'core', 'surface')
})

resid_corestats = table(rsaTable[,c("resName", "isCore")])
barplot(t(resid_corestats), col = c("cadetblue", "pink"), las=2)
legend("topright", legend = c("core", "surface"), fill = c("cadetblue", "pink"))

betafac = scan("tempFactor.csv", what = numeric())
betafac = betafac[44:269]
betafac = data.frame(resNo = 44:269, betafac = betafac)

plot(betafac$betafac, contactNo$contactNo, pch = 19, col = 'black',
     xlab = "beta factor",
     ylab = "coordination number")
abline(lm(contactNo$contactNo ~ betafac$betafac))
cor.test(betafac$betafac, contactNo$contactNo)

##  Pearson's product-moment correlation

# data:  betafac$betafac and contactNo$contactNo
# t = -9.0348, df = 224, p-value < 2.2e-16
# alternative hypothesis: true correlation is not equal to 0
# 95 percent confidence interval:
#  -0.6064040 -0.4142381
# sample estimates:
#        cor 
# -0.5168011 