def plotHistogramAndPdf(data, x, pdf):
    ax = plt.gca()
    plt.hist(data, bins=4, alpha=0.4, label='histogram of input values');
    plt.ylabel('Frequency')
    plt.xlabel('x values')
    ax2 = ax.twinx()
    plt.plot(x, pdf, c='red', label='probability density function');
    plt.ylabel('PDF')
    [tl.set_color('r') for tl in ax2.get_yticklabels()]
    ax.legend(bbox_to_anchor=(0.4, 1.15))
    ax2.legend(bbox_to_anchor=(1.15, 1.15))
    plt.savefig('figures/hist.jpg', bbox_inches='tight')

data = 'Corresponding variant data.csv'
plotHistogramAndPdf(data, x, true_pdf)

def getKernelDensityEstimation(values, x, bandwidth = 0.2, kernel = 'gaussian'):
    model = KernelDensity(kernel = kernel, bandwidth=bandwidth)
    model.fit(values[:, np.newaxis])
    log_density = model.score_samples(x[:, np.newaxis])
    return np.exp(log_density)
for bandwidth in np.linspace(0.2, 3, 3):
    kde = getKernelDensityEstimation(data, x, bandwidth=bandwidth)
    plt.plot(x, kde, alpha = 0.8, label = f'bandwidth = {round(bandwidth, 2)}')
plt.plot(x, true_pdf, label = 'True PDF')
plt.legend()
plt.title('Effect of various bandwidth values \nThe larger the bandwidth, the smoother the approximation becomes');
plt.savefig('figures/bw.jpg', bbox_inches='tight')

from statsmodels.nonparametric.bandwidths import bw_silverman, bw_scott, select_bandwidth
silverman_bandwidth = bw_silverman(data)
# select bandwidth allows to set a different kernel
silverman_bandwidth_gauss = select_bandwidth(data, bw = 'silverman', kernel = 'gauss')
scott_bandwidth = bw_scott(data)
def bestBandwidth(data, minBandwidth = 0.1, maxBandwidth = 2, nb_bandwidths = 30, cv = 30):
    """
    Run a cross validation grid search to identify the optimal bandwidth for the kernel density
    estimation.
    """
    from sklearn.model_selection import GridSearchCV
    model = GridSearchCV(KernelDensity(),
                        {'bandwidth': np.linspace(minBandwidth, maxBandwidth, nb_bandwidths)}, cv=cv)
    model.fit(data[:, None])
    return model.best_params_['bandwidth']
cv_bandwidth = bestBandwidth(data)
print(f"Silverman bandwidth = {silverman_bandwidth}")
print(f"Scott bandwidth = {scott_bandwidth}")
print(f"CV bandwidth = {cv_bandwidth}")

plt.figure(figsize= (14, 6))
plt.plot(x, true_pdf, label = 'True PDF')
kde = getKernelDensityEstimation(data, x, bandwidth=silverman_bandwidth)
plt.plot(x, kde, alpha = 0.8, label = f'Silverman bandwidth')
kde = getKernelDensityEstimation(data, x, bandwidth=scott_bandwidth)
plt.plot(x, kde, alpha = 0.8, label = f'Scott bandwidth')
kde = getKernelDensityEstimation(data, x, bandwidth=cv_bandwidth)
plt.plot(x, kde, alpha = 0.8, label = f'CV bandwidth')
plt.plot(x, stats_models_cv, alpha = 0.8, label = f'Statsmodels CV maximum likelihood')
plt.legend()
plt.title('Comparative of various bandwidth estimations for KDE');
plt.savefig('figures/comp_bw.jpg', bbox_inches='tight')