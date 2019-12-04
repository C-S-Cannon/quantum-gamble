import matplotlib.pyplot as plt
import numpy as np

# establish number of test cases
agN = 100000
jN = agN

alphaMu = 10.0
alphaSigma = 3.0

gammaMu = 0
gammaSigma = 20


# create array of alpha test case values according to gaussian distribution
alpha = np.random.normal(alphaMu, alphaSigma, agN)

# graph distribution of alpha
plt.subplot(2, 2, 1)
aCount, aBins, aIgnored = plt.hist(alpha, 30, density=True)
plt.plot(aBins, 1/(alphaSigma * np.sqrt(2 * np.pi)) *
         np.exp(- (aBins - alphaMu)**2 / (2 * alphaSigma**2)),
         linewidth=2, color='r')
plt.ylabel('Alpha')
plt.title('Input Error Distribution')
plt.yticks([])


# create array of gamma test case values according to gaussian distribution
gamma = np.random.normal(gammaMu, gammaSigma, agN)

# graph distribution of gamma
plt.subplot(2, 2, 3)
gCount, gBins, gIgnored = plt.hist(gamma, 30, density=True)
plt.plot(gBins, 1/(gammaSigma * np.sqrt(2 * np.pi)) *
         np.exp(- (gBins - gammaMu)**2 / (2 * gammaSigma**2)),
         linewidth=2, color='r')
plt.ylabel('Gamma')
plt.yticks([])


# fake jones matrix element function for testing
def testJones(alpha, gamma):
    return alpha * gamma


# repeat jones matrix calculation on random selections from above matrixs
jonesArr = np.empty(jN)
for i in range(jN):
    jonesArr[i] = testJones(alpha[np.random.randint(0, agN)],
                            gamma[np.random.randint(0, agN)])

# graph distribution of (pseudo) Jones using histogram buckets
plt.subplot(4, 2, 2)
xxCount, xxBins, xxIgnored = plt.hist(jonesArr, 30, density=True)
plt.ylabel('xx')
plt.title('Jones Matrix Values')
plt.yticks([])

plt.subplot(4, 2, 4)
xyCount, xyBins, xyIgnored = plt.hist(jonesArr, 30, density=True)
plt.ylabel('xy')
plt.yticks([])
plt.subplots_adjust(bottom=0.29)

plt.subplot(4, 2, 6)
yxCount, yxBins, yxIgnored = plt.hist(jonesArr, 30, density=True)
plt.ylabel('yx')
plt.yticks([])

plt.subplot(4, 2, 8)
yyCount, yyBins, yyIgnored = plt.hist(jonesArr, 30, density=True)
plt.ylabel('yy')
plt.yticks([])
plt.tight_layout()

# OR, animate new data point at each step, graph multiplicity vertically
# graph point to given x value, check to see if there is a nearby x point
# check if that point is at current y level, if yes, go up, then repeat
# points should "bubble up" to form a gaussian distribution

# also graph 2D with alpha/gamma and avg with error, the fuzzy blob graph

# calculate average and error from this new array of jones values
# will likely include an overall error and a per value error

# show graphs
plt.show()
