# Digit-Detection-using-Opencv
Handwritten Digit Recognition using OpenCV, mahotas, sklearn and Python 
# Dependencies
1. `cv2` 
2. `sklearn`
3. `skimage`
4. `numpy`
5. `mahotas` - `conda install -c conda-forge mahotas` / `conda install -c conda-forge/label/gcc7 mahotas` / `conda install -c conda-forge/label/broken mahotas` (any one if not found repo try one by one)
### I am using anaconda to go [here](https://repo.anaconda.com/archive/Anaconda3-5.3.1-Windows-x86_64.exe) then you create virtual_platform you need predefine packages in `.whl` file for windows [here](https://drive.google.com/file/d/1H5BacXAf2p7WuO9m3Qe9SqzMZAPSNCRi/view?usp=sharing) and for mac users [here](https://drive.google.com/open?id=1eC5HgN7nq1SgWrEzXgIutufynsp7UY04) i write all step by step installation procedure in .pdf file [here](https://drive.google.com/open?id=1DkrRxw_y1gh7fS1x0TOGtlqIeQZLAlhG)

open anaconda navigator then go `Environments section ` left click on the `base(root)` again left click on the play button select `open terminal`

`If you not installed previously don't go through `step 1.` directly jump on step 3.4 all fixes is done (3.1, 3.2, 3.3) for windows`

Step 1. `conda env remove -n virtual_platform (this erases the virtual platform and gives you a fresh start)`

Step 2. `got to https://pypi.python.org/pypi/torchvision and download torch vision, I suggest putting it in the same folder as the .yml that you will use in steps 3.1 to 3.4 `

Step 3. `fix:`

      1. `Open: virtual_platform_windows.yml  in an editor (eg Notepad++).`
      
      2. `Delete: line 92 (i.e. the line: - pytorch=0.1.12=py35_0.1.12cu80) and line 100 (- torch==0.1.12) `
      
      3. `Save`
      
      4. `Execute: conda env create -f virtual_platform_windows.yml`
      
      5. `Activate virtual environment: source activate virtual_platform`
      
      6. `Run an update of all the packages: conda update --all`
      
      7. `Install Pytorch seperately with: conda install -c peterjc123 pytorch cuda80`
      
Step 4. `Install torch vision with: pip install torchvision-0.2.0-py2.py3-none-any.whl`

# Contents
This repository contains the following files-

1. `train.py` - Python Script to create the classifier file `svm.pickle`.
2. `classify.py` - Python Script to test the classifier.
5. `classify_cam_input.py` - python Script to test the classifier using your web camera as input 
4. `svm.pickle` - Classifier file for digit recognition.
5. `imutils.py` - python Script contains required methods and it is self define.
5. `number.jpg` - Test image number 1 to test the classifier
6. `digits.jpg` - Test image numbre 2 to test the classifier

## Usage 

* Clone the repository - 
```bash
cd 
git clone https:https://github.com/Yogender-Singh/Digit-Detection-using-Opencv.git
cd Digit-Detection-using-Opencv
```
* The next step is to train the classifier. To do so run the script `train.py`. It will produce the classifier named `svm.pickle`. 

**NOTE** - *I have already created the `svm.pickle`, so this step is not necessary.*
```python
python train.py -dataset datasetName -m modelname.pickle
```
* To test the classifier, run the `classify.py` script.
```python
python classify.py -m modelName.pickle -i imageName.jpg
```
ex -
```python
python classify.py -m svm.pickle -i number.jpg
```
