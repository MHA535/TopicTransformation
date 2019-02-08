# TopicTransformation

Program that obtains document vector representations by using Topic Modeling* and Latent Dirichlet Allocation 

Requirements: Python +3.5, Gensim**, NLTK, and stop_words

Composed by two parts: Train/Load LDA model and Use LDA model to obtain document-vectors

`<files>` should be in the same level as `<default>`

Under `source.py` (`# LDA - Step`) you can control all LDA Hyper-parameters , including if you will run a standard LDA 
or Multi-core version*** of it


 #### Command execution examples

    # Train/Save - Produce Dictionary, MM and LDA Model
    python3 default/source.py --input files/input/test.txt --train True --output files/output/test.d --mmf files/output/test_corpus.mm --lda True --ldam files/output/lda_m.model --ldau True --docr files/train --docw files/output/result.txt
    
    # Load - Dictionary, MM and LDA Model
    python3 default/source.py --input files/input/test.txt --train False --output files/output/test.d --mmf files/output/test_corpus.mm --lda False --ldam files/output/lda_m.model --ldau False --docr files/train --docw files/output/result.txt
    
 `--train` - [True] It will produce Dictionary (based on corpus from input) and its Matrix Market format (MM).
 [False] Loads both of them

 `--input:` - Input folder-file: one document per line
 
 `--output` - Output for the Dictionary (`train = True`)trained or loaded (`train = False`)
 
 `--mmf` - Produce/Save corpus (input) in MM format (`train = True`) or load it (`train = False`)
 
 `--lda` - [True] Trains and save a LDA model using the dictionary and MM corpus. Adjust hyper parameters on `default/source.py`.
 [False] Load LDA model from `--ldam` location
           
 `--ldm` - Saves (`lda = True`) or Load (`lda = True`) LDA model
 
 `--ldau` - [True] Uses/Apply LDA model in documents from `--docr`. [False] Does not apply LDA model, exits the program
 
 `--docr` - Folder containing documents to apply LDA model. Classes for the documents are the sub-directory name
 
 `--docw` - Folder where translated documents are saved using csv format. One document per line in one single file,
 topics,dimensions separated by comma. Last feature is the class/label of the document. This format is useful for ML models.



*D. Blei et al. http://www.jmlr.org/papers/volume3/blei03a/blei03a.pdf)

** Gensim-LDA - https://radimrehurek.com/gensim/models/ldamodel.html

*** Multi-core LDA - https://rare-technologies.com/multicore-lda-in-python-from-over-night-to-over-lunch/)