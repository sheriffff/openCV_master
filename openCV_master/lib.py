import matplotlib.pyplot as plt
import cv2

def plot(*images, ncols=2, cv_imported=True):
    '''
    Plot several images in a grid
    cv_imported informs if images were imported via openCV, in which case we must change BGR to RGB
    '''
    if len(images) == 1:
        ncols = 1
        
    assert len(images) >= ncols, 'We must have #images >= #columns!!'
    
    nrows = (len(images) - 1) // ncols + 1
    
    fig, axes = plt.subplots(nrows=nrows, ncols=ncols)
    
    def _plot(ax, image, cv_imported):
        try:
            if cv_imported:
                ax.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
            else:
                ax.imshow(image)
        except:
            ax.imshow(image, cmap='gray')
    
    
    for i, image in enumerate(images):
        row = i // ncols
        col = i % ncols
        ax = axes[row, col] if len(images) > ncols else (axes if len(images) == 1 else axes[col])
        _plot(ax, image, cv_imported)