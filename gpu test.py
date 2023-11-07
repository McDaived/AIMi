import numpy as np
import cv2 as cv
import time

print('-'*101)

try:
    while True:
        npTmp = np.random.random((1024, 1024)).astype(np.float32)

        npMat1 = np.stack([npTmp, npTmp], axis=2)
        npMat2 = npMat1

        cuMat1 = cv.cuda_GpuMat()
        cuMat2 = cv.cuda_GpuMat()
        cuMat1.upload(npMat1)
        cuMat2.upload(npMat2)

        start_time = time.time()
        cv.cuda.gemm(cuMat1, cuMat2, 1, None, 0, None, 1)

        time_taken = time.time() - start_time
        print(f'|  CUDA using GPU --- {time_taken}' + ' '*(23-len(str(time_taken))) + 'seconds    |', end=' '*4)

        start_time = time.time()
        cv.gemm(npMat1, npMat2, 1, None, 0, None, 1)

        time_taken = time.time() - start_time
        print(f'CPU --- {time_taken}' + ' '*(22-len(str(time_taken))) +'seconds  |')

except KeyboardInterrupt:
    print(' '*39 + '|' + '\n' + '-'*101)








#Daived : I copy this gpu script from someone to test gpu if cuda works.