rsaTable <- read.table('/home/ece/Desktop/structuralBioinformatics/FinalTakeHome/1h68ASA',
                       fill = T, header = T)
rsaTable$isCore = sapply(rsaTable$Ratio, function(x){
  ifelse(x <= 5, 'core', 'surface')
})

resid_corestats = table(rsaTable[,c("Resname", "isCore")])
resid_percent <- data.frame(Core = resid_corestats[,1], Surface = resid_corestats[,2])
resid_percent$Core_p <-( resid_percent$Core/(resid_percent$Core + resid_percent$Surface))*100
resid_percent$sur_p <- (100 - resid_percent$Core_p)
hydrophobes <- c('ALA',  'LEU', 'VAL', 'PRO')
barplot(t(resid_percent[hydrophobes,3:4]), col = c("cadetblue", "pink"), las=2, horiz = T)
legend("topright", legend = c("core", "surface"), fill = c("cadetblue", "pink"))
  