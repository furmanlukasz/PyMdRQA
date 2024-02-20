import numpy as np
from pyrqa.time_series import TimeSeries
from pyrqa.neighbourhood import FixedRadius
from pyrqa.computation import RQAComputation
from pyrqa.settings import Settings
from pyrqa.metric import EuclideanMetric
from scipy.spatial.distance import pdist, squareform
from scipy.sparse import csr_matrix

def mdrqa(data, emb=1, delay=1, norm='non', radius=1):
    """
    Perform Multidimensional Recurrence Quantification Analysis (MdRQA)
    on a given dataset.
    
    :param data: N x M matrix, N data points in each time series, M time series
    :param emb: Embedding dimension
    :param delay: Delay for embedding
    :param norm: Normalization method (euc, min, max, non)
    :param radius: Radius for fixed neighbourhood
    :return: Dictionary with MdRQA results
    """
    # Compute and store parameter settings
    dims = data.shape[1]
    
    # Embedding if required
    if emb > 1:
        new_data = []
        for i in range(0, emb):
            new_data.append(data[i * delay:data.shape[0] - (emb - i - 1) * delay, :].flatten())
        data = np.column_stack(new_data)
    
    # Create distance matrix
    distance_matrix = squareform(pdist(data, 'euclidean'))
    
    # Apply norm and radius
    if norm == 'euc':
        distance_matrix /= np.mean(distance_matrix)
    elif norm == 'min':
        distance_matrix /= np.min(distance_matrix)
    elif norm == 'max':
        distance_matrix /= np.max(distance_matrix)
    
    # Thresholding the distance matrix to create the recurrence plot
    recurrence_matrix = distance_matrix < radius
    np.fill_diagonal(recurrence_matrix, 0)
    
    # Convert to a flat numpy array as required by PyRQA TimeSeries class
    flat_recurrence_matrix = recurrence_matrix.astype(np.float32).flatten()
    
    # Constructing the time series object for PyRQA
    time_series = TimeSeries(flat_recurrence_matrix,
                             embedding_dimension=emb,
                             time_delay=delay)
    
    # Define the settings for the RQA computation
    settings = Settings(time_series,
                        neighbourhood=FixedRadius(radius),
                        similarity_measure=EuclideanMetric(),
                        theiler_corrector=1)
    
    # Perform the RQA computation
    computation = RQAComputation.create(settings)
    result = computation.run()
    
    # Converting boolean matrix to sparse matrix format
    sparse_recurrence_matrix = csr_matrix(recurrence_matrix)
    
    output = {
        'SizeRP': recurrence_matrix.shape[0],
        'REC': result.recurrence_rate,
        'DET': result.determinism,
        'ADL': result.average_diagonal_line,
        'MDL': result.longest_diagonal_line,
        'DENTR': result.entropy_diagonal_lines,
        'LAM': result.laminarity,
        'MVL': result.longest_vertical_line,
        'VENTR': result.entropy_vertical_lines,
        'DIM': dims,
        'EMB': emb,
        'DEL': delay,
        'NORM': norm,
        'RAD': radius,
        'RP': sparse_recurrence_matrix
    }
    
    return output, recurrence_matrix

