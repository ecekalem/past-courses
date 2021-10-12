setwd('/home/ece/Desktop/')

chainU = read.table('4zksChainU.txt', header = T, row.names = NULL,
                    fill = T)
colnames(chainU)[1:2] = c('ResName', 'ResNo')

chainP = read.table('4zksChainP.txt', header = T, row.names = NULL,
                    fill = T)
colnames(chainP)[1:2] = c('ResName', 'ResNo')

complex = read.table('4zks_complex.txt', header = T, row.names = NULL,
                     fill = T)
colnames(complex)[1:2] = c('ResName', 'ResNo')


complex$chain = rep(c("U","P"), times = c(245,12))

chainUP_monomer = rbind(chainU, chainP)
chainUP_monomer$chain = complex$chain
any(chainUP_monomer$ResName != complex$ResName)

diff_total = chainUP_monomer$Total - complex$Total
diff_ratio = chainUP_monomer$Ratio... - complex$Ratio...

mean(diff_total > 1)
mean(diff_ratio > 1)

diffs = data.frame(total = diff_total, ratio = diff_ratio)
diffs$total_interface = diffs$total > 1
diffs$ratio_interface = diffs$ratio > 1

sum(diffs$total_interface == diffs$ratio_interface)

### extracting the residues of interface regions
interface_resids = subset(complex, diffs$ratio_interface)

chainU_interface = subset(interface_resids, chain == 'U')
chainP_interface = subset(interface_resids, chain == 'P')

setdiff(chainA_interface$ResNo, chainB_interface$ResNo)

chainU_interface$ResNo
35  41  42  57  60  60  60  99 143 146 151 189 190 191 192 193 195 213 215 216 219 220 226

chainP_interface$ResNo
2  3  4  5  6  7  8  9 10 11

###Interface propensity calculation 2.4

propensity <- sapply(unique(as.character(complex$ResName)), function(x){
(sum(interface_resids$ResName == x) / sum(complex$ResName == x)) / (nrow(interface_resids) / nrow(complex))
  
})
