#R < ex.edgeR --no-save
library(edgeR)

counts <- read.delim("edgeR_input.txt", row.names="Symbol")
#2 groups group 2 vs group 1.  Here each group has 18 samples
group <- factor(c(2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1))
cds <- DGEList(counts=counts,group=group)

# display summary of your samples
names(cds)
head(cds$counts)
cds$samples
sum(cds$all.zeros) # How many genes have 0 counts across all samples

# keep genes that achieve at least n (here 1) counts per million (cpm) in at least n (here 3) samples
keep <- rowSums(cpm(cds)>=1)>=3
cds <- cds[keep,]

# setting plot
postscript("R_plot.eps", paper="letter", horizontal=FALSE)  ####!!!!!!!!!!!!!!
par(mfrow=c(3,2))
par(omi=c(0.5,0.2,0.5,0.2), mai=c(0.8, 0.8, 0.8, 0.8))

# normalization and data exploration
cds <- calcNormFactors(cds)
cds$samples
cds <- calcNormFactors(cds, method="upperquartile")
cds$samples

plotMDS(cds, main="MDS Plot for Count Data", labels=colnames(cds$counts))

cds <- estimateCommonDisp(cds, verbose=TRUE)
cds <- estimateTagwiseDisp(cds)

plotBCV(cds)

meanVarPlot <- plotMeanVar(cds, show.raw.vars=TRUE, show.tagwise.vars=TRUE, show.binned.common.disp.vars=FALSE, show.ave.raw.vars=FALSE, NBline = TRUE , nbins = 100 , #these are arguments about what is plotted
    pch = 16 , xlab ="Mean Expression (Log10 Scale)" , ylab = "Variance (Log10 Scale)" , main = "Mean-Variance Plot" )

et <- exactTest(cds, pair=levels(group))
topTags(et)
top <- topTags(et, n=nrow(cds$counts))$table
head(top)

de <- rownames(top[top$FDR<0.05,])
length(de)
head(de)
hist(top$PValue, breaks=20)

plotSmear(cds , de.tags=de)
abline(h=c(-2, 2), col="blue")

plot(top$logFC, -log10(top$PValue), pch=20, cex=.5, ylab="-log10(p-value)", xlab="logFC", col=as.numeric(rownames(top) %in% de)+1)
abline(v=c(-2, 2), col="blue")

# output DEG and CPM to text files
mycpm <- cpm(cds, log=FALSE)  #### if log= TRUE output is logCPM
write.table(top, file="R_DEG.txt", sep='\t', quote=FALSE)  
write.table(mycpm, file="R_CPM.txt", sep='\t', quote=FALSE)
dev.off()

