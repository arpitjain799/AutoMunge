# Automunge Family Trees

![image](https://user-images.githubusercontent.com/44011748/76485571-4855b280-63f3-11ea-9574-c39a66e45e4e.png)

#  

## Introduction

Ok moving this portion of documentaiton from the README into a seperate file to try and improve the flow of rest of docuemtnation. This is intended as a resource to inspect transform_dict defined family trees associated with each root category in the section "Root Category Family Tree Definitions" as well as category properties associated with each category in the section "Category processdict Entries". 

Note that any of the family tree definitions can be overwritten in an automunge(.) call with the transformdict parameter and any of the category properties can be overwritten in an automunge(.) call with the processdict parameter.

For simplicity just going to copy the code directly from code base where these data structures are assembled. If you need to find a specific entry recomend applying a control-F search, e.g. to find entries for a root category 'string' can search for "{'string'".

## Table of Contents
* [Root Category Family Tree Definitions](https://github.com/Automunge/AutoMunge/blob/master/FamilyTrees.md#root-category-family-tree-definitions)
* [Category processdict Entries](https://github.com/Automunge/AutoMunge/blob/master/FamilyTrees.md#category-processdict-entries)

 ___ 
## Root Category Family Tree Definitions
```
  def _assembletransformdict(self, binstransform, NArw_marker):
    """
    #populates the transform_dict data structure
    #which is the internal library that is subsequently consolidated 
    #with any user passed transformdict
      
    #transform_dict is for purposes of populating
    #for each transformation category's use as a root category
    #a "family tree" set of associated transformation categories
    #which are for purposes of specifying the type and order of transformation functions
    #to be applied when a transformation category is assigned as a root category
      
    #we'll refer to the category key to a family as the "root category"
    #we'll refer to a transformation category entered into 
    #a family tree primitive as a "tree category"

    #a transformation category may serve as both a root category
    #and a tree category

    #each transformation category will have a set of properties assigned
    #in the corresponding process_dict data structure
    #including associated transformation functions, data properties, and etc.

    #a root category may be assigned to a column with the user passed assigncat
    #or when not specified may be determined under automation via _evalcategory

    #when applying transformations
    #the transformation functions associated with a root category
    #will not be applied unless that same category is populated as a tree category

    #the family tree primitives are for purposes of specifying order of transformations
    #as may include generations and branches of derivations
    #as well as for managing column retentions in the returned data
    #(as in some cases intermediate stages of transformations may or may not have desired retention)

    #the family tree primitives can be distinguished by types of 
    #upstream/downstream, supplement/replace, offsping/no offspring

    #___________
    #'parents' :
    #upstream / first generation / replaces column / with offspring

    #'siblings':
    #upstream / first generation / supplements column / with offspring

    #'auntsuncles' :
    #upstream / first generation / replaces column / no offspring

    #'cousins' :
    #upstream / first generation / supplements column / no offspring

    #'children' :
    #downstream parents / offspring generations / replaces column / with offspring

    #'niecesnephews' :
    #downstream siblings / offspring generations / supplements column / with offspring

    #'coworkers' :
    #downstream auntsuncles / offspring generations / replaces column / no offspring

    #'friends' :
    #downstream cousins / offspring generations / supplements column / no offspring
    #___________

    #each of the family tree primitives associated with a root category
    #may have entries of zero, one, or more transformation categories
      
    #when a root category is assigned to a column
    #the upstream primitives are inspected
      
    #when a tree category is found 
    #as an entry to an upstream primitive associated with the root category
    #the transformation functions associated with the tree category are performed

    #if any tree categories are populated in the upstream replacement primitives
    #their inclusion supercedes supplement primitive entries
    #and so the input column to the transformation is not retained in the returned set
    #with the column replacement either achieved by an inplace transformation
    #or subsequent deletion operation

    #when a tree category is found
    #as an entry to an upstream primitive with offspring
    #after the associated transformation function is performed
    #the downstream primitives of the family tree of the tree category is inspected
    #and those downstream primitives are treated as a subsequent generation's upstream primitives
    #where the input column to that subsequent generation is the column returned 
    #from the transformation function associated with the upstream tree category

    #this is an easy point of confusion so as further clarification on this point
    #the downstream primitives associated with a root category
    #will not be inspected when root category is applied
    #unless that root category is also entered as a tree category entry
    #in one of the root category's upstream primitives with offspring
    """

    transform_dict = {}

    #initialize bins based on what was passed through application of automunge(.)
    if binstransform is True:
      bint = 'bint'
    else:
      bint = None
        
    if NArw_marker is True:
      NArw = 'NArw'
    else:
      NArw = None

    #initialize trasnform_dict. Note in a future extension the range of categories
    #is intended to be built out
    transform_dict.update({'nmbr' : {'parents'       : ['nmbr'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : [bint]}})
    
    transform_dict.update({'dxdt' : {'parents'       : ['dxdt'],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['retn'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['retn'],
                                     'friends'       : []}})
    
    transform_dict.update({'d2dt' : {'parents'       : ['d2dt'],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['retn'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : ['dxdt'],
                                     'coworkers'     : ['retn'],
                                     'friends'       : []}})
    
    transform_dict.update({'d3dt' : {'parents'       : ['d3dt'],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['retn'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : ['d2dt'],
                                     'coworkers'     : ['retn'],
                                     'friends'       : []}})

    transform_dict.update({'d4dt' : {'parents'       : ['d4dt'],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['retn'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : ['d3dt'],
                                     'coworkers'     : ['retn'],
                                     'friends'       : []}})

    transform_dict.update({'d5dt' : {'parents'       : ['d5dt'],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['retn'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : ['d4dt'],
                                     'coworkers'     : ['retn'],
                                     'friends'       : []}})

    transform_dict.update({'d6dt' : {'parents'       : ['d6dt'],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['retn'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : ['d5dt'],
                                     'coworkers'     : ['retn'],
                                     'friends'       : []}})
    
    transform_dict.update({'dxd2' : {'parents'       : ['dxd2'],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['retn'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['retn'],
                                     'friends'       : []}})
    
    transform_dict.update({'d2d2' : {'parents'       : ['d2d2'],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['retn'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : ['dxd2'],
                                     'coworkers'     : ['retn'],
                                     'friends'       : []}})
    
    transform_dict.update({'d3d2' : {'parents'       : ['d3d2'],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['retn'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : ['d2d2'],
                                     'coworkers'     : ['retn'],
                                     'friends'       : []}})

    transform_dict.update({'d4d2' : {'parents'       : ['d4d2'],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['retn'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : ['d3d2'],
                                     'coworkers'     : ['retn'],
                                     'friends'       : []}})

    transform_dict.update({'d5d2' : {'parents'       : ['d5d2'],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['retn'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : ['d4d2'],
                                     'coworkers'     : ['retn'],
                                     'friends'       : []}})

    transform_dict.update({'d6d2' : {'parents'       : ['d6d2'],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['retn'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : ['d5d2'],
                                     'coworkers'     : ['retn'],
                                     'friends'       : []}})
    
    transform_dict.update({'nmdx' : {'parents'       : ['nmdx'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : ['dxdt'],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['retn'],
                                     'friends'       : []}})
    
    transform_dict.update({'nmd2' : {'parents'       : ['nmd2'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : ['d2dt'],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['retn'],
                                     'friends'       : []}})
    
    transform_dict.update({'nmd3' : {'parents'       : ['nmd3'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : ['d3dt'],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['retn'],
                                     'friends'       : []}})

    transform_dict.update({'nmd4' : {'parents'       : ['nmd4'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : ['d4dt'],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['retn'],
                                     'friends'       : []}})

    transform_dict.update({'nmd5' : {'parents'       : ['nmd5'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : ['d5dt'],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['retn'],
                                     'friends'       : []}})

    transform_dict.update({'nmd6' : {'parents'       : ['nmd6'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : ['d6dt'],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['retn'],
                                     'friends'       : []}})
    
    transform_dict.update({'mmdx' : {'parents'       : ['mmdx'],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['nbr2'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['nbr2'],
                                     'friends'       : []}})
    
    transform_dict.update({'mmd2' : {'parents'       : ['mmd2'],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['nbr2'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : ['mmdx'],
                                     'coworkers'     : ['nbr2'],
                                     'friends'       : []}})
    
    transform_dict.update({'mmd3' : {'parents'       : ['mmd3'],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['nbr2'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : ['mmd2'],
                                     'coworkers'     : ['nbr2'],
                                     'friends'       : []}})

    transform_dict.update({'mmd4' : {'parents'       : ['mmd4'],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['nbr2'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : ['mmd3'],
                                     'coworkers'     : ['nbr2'],
                                     'friends'       : []}})

    transform_dict.update({'mmd5' : {'parents'       : ['mmd5'],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['nbr2'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : ['mmd4'],
                                     'coworkers'     : ['nbr2'],
                                     'friends'       : []}})

    transform_dict.update({'mmd6' : {'parents'       : ['mmd6'],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['nbr2'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : ['mmd5'],
                                     'coworkers'     : ['nbr2'],
                                     'friends'       : []}})
    
    transform_dict.update({'dddt' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['dddt', 'exc2'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'ddd2' : {'parents'       : ['ddd2'],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['exc2'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : ['dddt'],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'ddd3' : {'parents'       : ['ddd3'],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['exc2'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : ['ddd2'],
                                     'coworkers'     : [],
                                     'friends'       : []}})

    transform_dict.update({'ddd4' : {'parents'       : ['ddd4'],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['exc2'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : ['ddd3'],
                                     'coworkers'     : [],
                                     'friends'       : []}})

    transform_dict.update({'ddd5' : {'parents'       : ['ddd5'],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['exc2'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : ['ddd4'],
                                     'coworkers'     : [],
                                     'friends'       : []}})

    transform_dict.update({'ddd6' : {'parents'       : ['ddd6'],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['exc2'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : ['ddd5'],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'dedt' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['dedt', 'exc2'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'ded2' : {'parents'       : ['ded2'],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['exc2'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : ['dedt'],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'ded3' : {'parents'       : ['ded3'],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['exc2'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : ['ded2'],
                                     'coworkers'     : [],
                                     'friends'       : []}})

    transform_dict.update({'ded4' : {'parents'       : ['ded4'],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['exc2'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : ['ded3'],
                                     'coworkers'     : [],
                                     'friends'       : []}})

    transform_dict.update({'ded5' : {'parents'       : ['ded5'],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['exc2'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : ['ded4'],
                                     'coworkers'     : [],
                                     'friends'       : []}})

    transform_dict.update({'ded6' : {'parents'       : ['ded6'],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['exc2'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : ['ded5'],
                                     'coworkers'     : [],
                                     'friends'       : []}})

    transform_dict.update({'shft' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['shft'],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
  
    transform_dict.update({'shf2' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['shf2'],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'shf3' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['shf3'],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})

    transform_dict.update({'shf4' : {'parents'       : ['shf4'],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['retn'],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['retn'],
                                     'friends'       : []}})
  
    transform_dict.update({'shf5' : {'parents'       : ['shf5'],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['retn'],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['retn'],
                                     'friends'       : []}})
    
    transform_dict.update({'shf6' : {'parents'       : ['shf6'],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['retn'],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['retn'],
                                     'friends'       : []}})

    transform_dict.update({'shf7' : {'parents'       : ['shf4', 'shf5'],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['retn'],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['retn'],
                                     'friends'       : []}})
    
    transform_dict.update({'shf8' : {'parents'       : ['shf4', 'shf5', 'shf6'],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['retn'],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['retn'],
                                     'friends'       : []}})

    transform_dict.update({'bnry' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['bnry'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'bnr2' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['bnr2'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})

    transform_dict.update({'onht' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['onht'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'text' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['text'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'txt2' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['text'],
                                     'cousins'       : [NArw, 'splt'],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'txt3' : {'parents'       : ['txt3'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['text'],
                                     'friends'       : []}})

    transform_dict.update({'smth' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['smth'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
  
    transform_dict.update({'fsmh' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['fsmh'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})

    transform_dict.update({'lngt' : {'parents'       : ['lngt'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['mnmx'],
                                     'friends'       : []}})
  
    transform_dict.update({'lnlg' : {'parents'       : ['lnlg'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['log0'],
                                     'friends'       : []}})

    transform_dict.update({'UPCS' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['UPCS'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'Unht' : {'parents'       : ['Unht'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['onht'],
                                     'friends'       : []}})
  
    transform_dict.update({'Utxt' : {'parents'       : ['Utxt'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['text'],
                                     'friends'       : []}})
    
    transform_dict.update({'Utx2' : {'parents'       : ['Utx2'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['text'],
                                     'friends'       : ['splt']}})

    transform_dict.update({'Utx3' : {'parents'       : ['Utx3'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : ['txt3'],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'Ucct' : {'parents'       : ['Ucct'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['ucct', 'ord3'],
                                     'friends'       : []}})
    
    transform_dict.update({'Uord' : {'parents'       : ['Uord'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['ordl'],
                                     'friends'       : []}})
        
    transform_dict.update({'Uor2' : {'parents'       : ['Uor2'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : ['ord2'],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'Uor3' : {'parents'       : ['Uor3'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['ord3'],
                                     'friends'       : []}})
    
    transform_dict.update({'Uor6' : {'parents'       : ['Uor6'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : ['spl6'],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['ord3'],
                                     'friends'       : []}})
    
    transform_dict.update({'U101' : {'parents'       : ['U101'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['1010'],
                                     'friends'       : []}})
    
    transform_dict.update({'splt' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['splt'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'spl2' : {'parents'       : ['spl2'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['ord3'],
                                     'friends'       : []}})
    
    transform_dict.update({'spl5' : {'parents'       : ['spl5'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['ord3'],
                                     'friends'       : []}})
    
    transform_dict.update({'spl6' : {'parents'       : ['spl6'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : ['splt'],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : ['ord3']}})
    
    transform_dict.update({'spl7' : {'parents'       : ['spl7'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['ord3'],
                                     'friends'       : []}})

    transform_dict.update({'spl8' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['spl8'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})

    transform_dict.update({'spl9' : {'parents'       : ['spl9'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['ord3'],
                                     'friends'       : []}})

    transform_dict.update({'sp10' : {'parents'       : ['sp10'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['ord3'],
                                     'friends'       : []}})
    
    transform_dict.update({'sp11' : {'parents'       : ['sp11'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : ['spl5'],
                                     'coworkers'     : ['ord3'],
                                     'friends'       : []}})
    
    transform_dict.update({'sp12' : {'parents'       : ['sp12'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : ['sp11'],
                                     'coworkers'     : ['ord3'],
                                     'friends'       : []}})
    
    transform_dict.update({'sp13' : {'parents'       : ['sp13'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : ['sp10'],
                                     'coworkers'     : ['ord3'],
                                     'friends'       : []}})
    
    transform_dict.update({'sp14' : {'parents'       : ['sp14'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : ['sp13'],
                                     'coworkers'     : ['ord3'],
                                     'friends'       : []}})
    
    transform_dict.update({'sp15' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['sp15'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
  
    transform_dict.update({'sp16' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['sp16'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'sp17' : {'parents'       : ['sp17'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : ['spl5'],
                                     'coworkers'     : ['ord3'],
                                     'friends'       : []}})
    
    transform_dict.update({'sp18' : {'parents'       : ['sp18'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : ['sp17'],
                                     'coworkers'     : ['ord3'],
                                     'friends'       : []}})

    transform_dict.update({'sp19' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['sp19'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})

    transform_dict.update({'sp20' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['sp20'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})

    transform_dict.update({'sbst' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['sbst'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})

    transform_dict.update({'sbs2' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['sbs2'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})

    transform_dict.update({'sbs3' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['sbs3'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})

    transform_dict.update({'sbs4' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['sbs4'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})

    transform_dict.update({'hash' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['hash'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})

    transform_dict.update({'hsh2' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['hsh2'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'hs10' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['hs10'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'Uhsh' : {'parents'       : ['Uhsh'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['hash'],
                                     'friends'       : []}})

    transform_dict.update({'Uhs2' : {'parents'       : ['Uhs2'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['hsh2'],
                                     'friends'       : []}})
    
    transform_dict.update({'Uh10' : {'parents'       : ['Uh10'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['hs10'],
                                     'friends'       : []}})
    
    transform_dict.update({'srch' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['srch'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
  
    transform_dict.update({'src2' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['src2'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'src3' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['src3'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'src4' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['src4'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'aggt' : {'parents'       : ['aggt'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['ord3'],
                                     'friends'       : []}})
    
    transform_dict.update({'strn' : {'parents'       : ['strn'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['ord3'],
                                     'friends'       : []}})

    transform_dict.update({'strg' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['strg'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'nmrc' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['nmrc'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
  
    transform_dict.update({'nmr2' : {'parents'       : ['nmr2'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : ['nmbr'],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'nmr3' : {'parents'       : ['nmr3'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : ['mnmx'],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})

    transform_dict.update({'nmr4' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['nmr4'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
  
    transform_dict.update({'nmr5' : {'parents'       : ['nmr5'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : ['nmbr'],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'nmr6' : {'parents'       : ['nmr6'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : ['mnmx'],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'nmr7' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['nmr7'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
  
    transform_dict.update({'nmr8' : {'parents'       : ['nmr8'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : ['nmbr'],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'nmr9' : {'parents'       : ['nmr9'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : ['mnmx'],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'nmcm' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['nmcm'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
  
    transform_dict.update({'nmc2' : {'parents'       : ['nmc2'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : ['nmbr'],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'nmc3' : {'parents'       : ['nmc3'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : ['mnmx'],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})

    transform_dict.update({'nmc4' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['nmc4'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
  
    transform_dict.update({'nmc5' : {'parents'       : ['nmc5'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : ['nmbr'],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'nmc6' : {'parents'       : ['nmc6'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : ['mnmx'],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})

    transform_dict.update({'nmc7' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['nmc7'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
  
    transform_dict.update({'nmc8' : {'parents'       : ['nmc8'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : ['nmbr'],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'nmc9' : {'parents'       : ['nmc9'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : ['mnmx'],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'nmEU' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['nmEU'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
  
    transform_dict.update({'nmE2' : {'parents'       : ['nmE2'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : ['nmbr'],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'nmE3' : {'parents'       : ['nmE3'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : ['mnmx'],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'nmE4' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['nmE4'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
  
    transform_dict.update({'nmE5' : {'parents'       : ['nmE5'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : ['nmbr'],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'nmE6' : {'parents'       : ['nmE6'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : ['mnmx'],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'nmE7' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['nmE7'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
  
    transform_dict.update({'nmE8' : {'parents'       : ['nmE8'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : ['nmbr'],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'nmE9' : {'parents'       : ['nmE9'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : ['mnmx'],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'ors7' : {'parents'       : ['spl6', 'nmr2'],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['ord3'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'ors5' : {'parents'       : ['spl5'],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['ord3'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'ors6' : {'parents'       : ['spl6'],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['ord3'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'ordl' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['ordl'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
        
    transform_dict.update({'ord2' : {'parents'       : ['ord2'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['mnmx'],
                                     'friends'       : []}})
    
    transform_dict.update({'ord3' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['ord3'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})

    transform_dict.update({'ord5' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['ord5'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})

    transform_dict.update({'maxb' : {'parents'       : ['or3b'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
  
    transform_dict.update({'or3b' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['or3b'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['maxb'],
                                     'friends'       : []}})
  
    transform_dict.update({'matx' : {'parents'       : ['or3c'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['onht'],
                                     'friends'       : []}})
    
    transform_dict.update({'or3c' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['or3c'],
                                     'cousins'       : [NArw],
                                     'children'      : ['matx'],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'ma10' : {'parents'       : ['or3d'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['1010'],
                                     'friends'       : []}})
    
    transform_dict.update({'or3d' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['or3d'],
                                     'cousins'       : [NArw],
                                     'children'      : ['ma10'],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'ucct' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['ucct'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
        
    transform_dict.update({'ord4' : {'parents'       : ['ord4'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['mnmx'],
                                     'friends'       : []}})
    
    transform_dict.update({'ors2' : {'parents'       : ['spl2'],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['ord3'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'or10' : {'parents'       : ['ord4'],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['1010'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['mnmx'],
                                     'friends'       : []}})
    
    transform_dict.update({'or11' : {'parents'       : ['sp11'],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['1010'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
  
    transform_dict.update({'or12' : {'parents'       : ['nmr2'],
                                     'siblings'      : ['sp11'],
                                     'auntsuncles'   : ['1010'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'or13' : {'parents'       : ['sp12'],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['1010'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'or14' : {'parents'       : ['nmr2'],
                                     'siblings'      : ['sp12'],
                                     'auntsuncles'   : ['1010'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})

    transform_dict.update({'or15' : {'parents'       : ['or15'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : ['sp13'],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['1010'],
                                     'friends'       : []}})
  
    transform_dict.update({'or16' : {'parents'       : ['or16'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : ['nmr2'],
                                     'niecesnephews' : ['sp13'],
                                     'coworkers'     : ['1010'],
                                     'friends'       : []}})
    
    transform_dict.update({'or17' : {'parents'       : ['or17'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : ['sp14'],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['1010'],
                                     'friends'       : []}})
    
    transform_dict.update({'or18' : {'parents'       : ['or18'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : ['nmr2'],
                                     'niecesnephews' : ['sp14'],
                                     'coworkers'     : ['1010'],
                                     'friends'       : []}})

    transform_dict.update({'or19' : {'parents'       : ['or19'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : ['nmc8'],
                                     'niecesnephews' : ['sp13'],
                                     'coworkers'     : ['1010'],
                                     'friends'       : []}})
    
    transform_dict.update({'or20' : {'parents'       : ['or20'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : ['nmc8'],
                                     'niecesnephews' : ['sp14'],
                                     'coworkers'     : ['1010'],
                                     'friends'       : []}})
    
    transform_dict.update({'or21' : {'parents'       : ['or21'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : ['nmc8'],
                                     'niecesnephews' : ['sp17'],
                                     'coworkers'     : ['1010'],
                                     'friends'       : []}})
    
    transform_dict.update({'or22' : {'parents'       : ['or22'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : ['nmc8'],
                                     'niecesnephews' : ['sp18'],
                                     'coworkers'     : ['1010'],
                                     'friends'       : []}})

    transform_dict.update({'or23' : {'parents'       : ['or23'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['nmcm', 'sp19', 'ord3'],
                                     'friends'       : []}})
    
    transform_dict.update({'om10' : {'parents'       : ['ord4'],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['1010', 'mnmx'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['mnmx'],
                                     'friends'       : []}})

    transform_dict.update({'mmor' : {'parents'       : ['ord4'],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['mnmx'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'1010' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['1010'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})

    transform_dict.update({'null' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['null'],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'NArw' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['NArw'],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'NAr2' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['NAr2'],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'NAr3' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['NAr3'],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'NAr4' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['NAr4'],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'NAr5' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['NAr5'],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'nbr2' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['nmbr'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'nbr3' : {'parents'       : ['nbr3'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : ['bint']}})
    
    transform_dict.update({'MADn' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['MADn'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'MAD2' : {'parents'       : ['MAD2'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : ['nmbr'],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'MAD3' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['MAD3'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'mnmx' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['mnmx'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'mnm2' : {'parents'       : ['nmbr'],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['mnmx'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'mnm3' : {'parents'       : ['nmbr'],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['mnm3'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'mnm4' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['mnm3'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'mnm5' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['mnmx'],
                                     'cousins'       : ['nmbr', NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'mnm6' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['mnm6'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'mnm7' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['mnmx', 'bins'],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})

    transform_dict.update({'mxab' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['mxab'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'retn' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['retn'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})

    transform_dict.update({'rtbn' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['retn', 'bsor'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})

    transform_dict.update({'rtb2' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['retn', 'bins'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})

    transform_dict.update({'mean' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['mean'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'mea2' : {'parents'       : ['nmbr'],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['mean'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'mea3' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['mean', 'bins'],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})

    transform_dict.update({'tmsc' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['tmsc'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})

    transform_dict.update({'time' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['time'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})

    transform_dict.update({'tmzn' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['tmzn'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})

    transform_dict.update({'date' : {'parents'       : ['date'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['year', 'mnth', 'days', 'hour', 'mint', 'scnd'],
                                     'friends'       : []}})
  
    transform_dict.update({'dat2' : {'parents'       : ['dat2'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['bshr', 'wkdy', 'hldy'],
                                     'friends'       : []}})
    
    transform_dict.update({'dat3' : {'parents'       : ['dat3'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['year', 'mnsn', 'mncs', 'dysn', 'dycs', 'hrsn', 'hrcs', 'misn', 'mics', 'scsn', 'sccs'],
                                     'friends'       : []}})
    
    transform_dict.update({'dat4' : {'parents'       : ['dat4'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['year', 'mdsn', 'mdcs', 'hmss', 'hmsc'],
                                     'friends'       : []}})
    
    transform_dict.update({'dat5' : {'parents'       : ['dat5'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['year', 'mdsn', 'mdcs', 'dysn', 'dycs', 'hmss', 'hmsc'],
                                     'friends'       : []}})
    
    transform_dict.update({'dat6' : {'parents'       : ['dat6'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['year', 'mdsn', 'mdcs', 'hmss', 'hmsc', 'bshr', 'wkdy', 'hldy'],
                                     'friends'       : []}})
    
    transform_dict.update({'year' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['year'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
  
    transform_dict.update({'yea2' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['year', 'yrsn', 'yrcs', 'mdsn', 'mdcs'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})

    transform_dict.update({'yrcs' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['yrcs'],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'yrsn' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['yrsn'],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'mnth' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['mnth'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
  
    transform_dict.update({'mnt2' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['mnsn', 'mncs'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'mnt3' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['mnsn', 'mncs', 'dysn', 'dycs', 'hrsn', 'hrcs', 'misn', 'mics', 'scsn', 'sccs'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'mnt4' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['mdsn', 'mdcs'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'mnt5' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['mdsn', 'mdcs', 'hmss', 'hmsc'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'mnt6' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['mdsn', 'mdcs', 'dysn', 'dycs', 'hmss', 'hmsc'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'mnsn' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['mnsn'],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'mncs' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['mncs'],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'mdsn' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['mdsn'],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'mdcs' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['mdcs'],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})

    transform_dict.update({'days' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['days'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
  
    transform_dict.update({'day2' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['dysn', 'dycs'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'day3' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['dysn', 'dycs', 'hrsn', 'hrcs', 'misn', 'mics', 'scsn', 'sccs'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'day4' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['dhms', 'dhmc'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'day5' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['dhms', 'dhmc', 'hmss', 'hmsc'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'dysn' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['dysn'],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'dycs' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['dycs'],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'dhms' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['dhms'],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'dhmc' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['dhmc'],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'hour' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['hour'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
  
    transform_dict.update({'hrs2' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['hrsn', 'hrcs'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'hrs3' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['hrsn', 'hrcs', 'misn', 'mics', 'scsn', 'sccs'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'hrs4' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['hmss', 'hmsc'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'hrsn' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['hrsn'],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'hrcs' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['hrcs'],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'hmss' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['hmss'],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'hmsc' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['hmsc'],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'mint' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['mint'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
  
    transform_dict.update({'min2' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['misn', 'mics'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'min3' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['misn', 'mics', 'scsn', 'sccs'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'min4' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['mssn', 'mscs'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'misn' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['misn'],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'mics' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['mics'],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'mssn' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['mssn'],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'mscs' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['mscs'],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})

    transform_dict.update({'scnd' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['scnd'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
  
    transform_dict.update({'scn2' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['scsn', 'sccs'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'scsn' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['scsn'],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'sccs' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['sccs'],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})

    transform_dict.update({'qttf' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['qttf'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
  
    transform_dict.update({'qtt2' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['qtt2'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'bxcx' : {'parents'       : ['bxcx'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : ['nmbr'],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'bxc2' : {'parents'       : ['bxc2'],
                                     'siblings'      : ['nmbr'],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : ['nmbr'],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'bxc3' : {'parents'       : ['bxc3'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : ['nmbr'],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'bxc4' : {'parents'       : ['bxc4'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['nbr2'],
                                     'friends'       : []}})

    transform_dict.update({'bxc5' : {'parents'       : ['bxc5'],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['mnmx'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['nbr2', 'bins'],
                                     'friends'       : []}})

    transform_dict.update({'ntgr' : {'parents'       : ['ntgr'],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['retn', '1010', 'ordl'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['mnmx'],
                                     'friends'       : []}})
    
    transform_dict.update({'ntg2' : {'parents'       : ['ntg2'],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['retn', '1010', 'ordl', 'pwr2'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['mnmx'],
                                     'friends'       : []}})
    
    transform_dict.update({'ntg3' : {'parents'       : ['ntg3'],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['retn', 'ordl', 'por2'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['mnmx'],
                                     'friends'       : []}})
    
    transform_dict.update({'pwrs' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['pwrs'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'pwr2' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['pwr2'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'log0' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['log0'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'log1' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['log0', 'pwr2'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'logn' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['logn'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
  
    transform_dict.update({'lgnm' : {'parents'       : ['lgnm'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['nmbr'],
                                     'friends'       : []}})
    
    transform_dict.update({'sqrt' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['sqrt'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'addd' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['addd'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
  
    transform_dict.update({'sbtr' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['sbtr'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'mltp' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['mltp'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'divd' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['divd'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'rais' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['rais'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'absl' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['absl'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'bkt1' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['bkt1'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'bkt2' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['bkt2'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'bkt3' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['bkt3'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'bkt4' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['bkt4'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'wkdy' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['wkdy'],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'bshr' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['bshr'],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'hldy' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['hldy'],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'wkds' : {'parents'       : ['wkds'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['text'],
                                     'friends'       : []}})
  
    transform_dict.update({'wkdo' : {'parents'       : ['wkdo'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['ordl'],
                                     'friends'       : []}})
    
    transform_dict.update({'mnts' : {'parents'       : ['mnts'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['text'],
                                     'friends'       : []}})
  
    transform_dict.update({'mnto' : {'parents'       : ['mnto'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['ordl'],
                                     'friends'       : []}})
    
    transform_dict.update({'bins' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['bins'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})

    transform_dict.update({'bint' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['bint'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'bsor' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['bsor'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})

    transform_dict.update({'btor' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['btor'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'bnwd' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['bnwd'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'bnwK' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['bnwK'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
  
    transform_dict.update({'bnwM' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['bnwM'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'bnwo' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['bnwo'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
  
    transform_dict.update({'bnKo' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['bnKo'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'bnMo' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['bnMo'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})    
    
    transform_dict.update({'bnep' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['bnep'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'bne7' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['bne7'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'bne9' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['bne9'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'bneo' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['bneo'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'bn7o' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['bn7o'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})

    transform_dict.update({'bn9o' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['bn9o'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'tlbn' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['tlbn'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'pwor' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['pwor'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'por2' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['por2'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})

    transform_dict.update({'por3' : {'parents'       : ['por3'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['1010'],
                                     'friends'       : []}})

    transform_dict.update({'bkb3' : {'parents'       : ['bkb3'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['1010'],
                                     'friends'       : []}})
  
    transform_dict.update({'bkb4' : {'parents'       : ['bkb4'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['1010'],
                                     'friends'       : []}})
    
    transform_dict.update({'bsbn' : {'parents'       : ['bsbn'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['1010'],
                                     'friends'       : []}})
    
    transform_dict.update({'bnwb' : {'parents'       : ['bnwb'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['1010'],
                                     'friends'       : []}})
    
    transform_dict.update({'bnKb' : {'parents'       : ['bnKb'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['1010'],
                                     'friends'       : []}})

    transform_dict.update({'bnMb' : {'parents'       : ['bnMb'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['1010'],
                                     'friends'       : []}})
    
    transform_dict.update({'bneb' : {'parents'       : ['bneb'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['1010'],
                                     'friends'       : []}})

    transform_dict.update({'bn7b' : {'parents'       : ['bn7b'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['1010'],
                                     'friends'       : []}})
    
    transform_dict.update({'bn9b' : {'parents'       : ['bn9b'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['1010'],
                                     'friends'       : []}})
    
    transform_dict.update({'pwbn' : {'parents'       : ['pwbn'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['1010'],
                                     'friends'       : []}})

    transform_dict.update({'DPnb' : {'parents'       : ['DPn3'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'DPn3' : {'parents'       : ['DPn3'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['DPnb'],
                                     'friends'       : []}})

    transform_dict.update({'DPmm' : {'parents'       : ['DPm2'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
  
    transform_dict.update({'DPm2' : {'parents'       : ['DPm2'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['DPmm'],
                                     'friends'       : []}})

    transform_dict.update({'DPrt' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['DPrt'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})

    transform_dict.update({'DLnb' : {'parents'       : ['DLn3'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'DLn3' : {'parents'       : ['DLn3'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['DLnb'],
                                     'friends'       : []}})

    transform_dict.update({'DLmm' : {'parents'       : ['DLm2'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
  
    transform_dict.update({'DLm2' : {'parents'       : ['DLm2'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['DLmm'],
                                     'friends'       : []}})

    transform_dict.update({'DLrt' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['DLrt'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
  
    transform_dict.update({'DPbn' : {'parents'       : ['DPb2'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'DPb2' : {'parents'       : ['DPb2'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['DPbn'],
                                     'friends'       : []}})
    
    transform_dict.update({'DPod' : {'parents'       : ['DPo4'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'DPo4' : {'parents'       : ['DPo4'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['DPod'],
                                     'friends'       : []}})
    
    transform_dict.update({'DPoh' : {'parents'       : ['DPo5'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : ['onht'],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'DPo5' : {'parents'       : ['DPo5'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : ['DPo2'],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'DPo2' : {'parents'       : ['DPo2'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['onht'],
                                     'friends'       : []}})
    
    transform_dict.update({'DP10' : {'parents'       : ['DPo6'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : ['1010'],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'DPo6' : {'parents'       : ['DPo6'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : ['DPo3'],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'DPo3' : {'parents'       : ['DPo3'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['1010'],
                                     'friends'       : []}})

    transform_dict.update({'qbt1' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['qbt1'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
  
    transform_dict.update({'qbt2' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['qbt2'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'qbt3' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['qbt3'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'qbt4' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['qbt4'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})

    transform_dict.update({'nmqb' : {'parents'       : ['nmqb'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['qbt1'],
                                     'friends'       : []}})
  
    transform_dict.update({'nmq2' : {'parents'       : ['nmq2'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : ['qbt1']}})
  
    transform_dict.update({'mmqb' : {'parents'       : ['mmqb'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['qbt3'],
                                     'friends'       : []}})
    
    transform_dict.update({'mmq2' : {'parents'       : ['mmq2'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : ['qbt3']}})
    
    transform_dict.update({'copy' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['copy'],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'excl' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['excl'],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'exc2' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['exc2'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'exc3' : {'parents'       : ['exc3'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : ['bins']}})
    
    transform_dict.update({'exc4' : {'parents'       : ['exc4'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : ['pwr2']}})
    
    transform_dict.update({'exc5' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['exc5'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})

    transform_dict.update({'exc6' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['exc2'],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})

    transform_dict.update({'exc7' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['exc5'],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})

    transform_dict.update({'exc8' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['exc5'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})

    transform_dict.update({'exc9' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['exc5'],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'shfl' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['shfl'],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})

    transform_dict.update({'nmbd' : {'parents'       : ['nmbr'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : [bint]}})

    transform_dict.update({'101d' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['1010'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'ordd' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['ord3'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'texd' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['text'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'bnrd' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['bnry'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'datd' : {'parents'       : ['datd'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['year', 'mdsn', 'mdcs', 'hmss', 'hmsc', 'bshr', 'wkdy', 'hldy'],
                                     'friends'       : []}})
    
    transform_dict.update({'nuld' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['null'],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'lbnm' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['exc2'],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})

    transform_dict.update({'lbnb' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['nmbr'],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})

    transform_dict.update({'lb10' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['1010'],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'lbor' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['ordl'],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})

    transform_dict.update({'lbos' : {'parents'       : ['lbos'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['strg'],
                                     'friends'       : []}})
    
    transform_dict.update({'lbte' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['text'],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'lbbn' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['bnry'],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})

    transform_dict.update({'lbsm' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['lbsm'],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
  
    transform_dict.update({'lbfs' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['lbfs'],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'lbda' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['year', 'mdsn', 'mdcs', 'hmss', 'hmsc', 'bshr', 'wkdy', 'hldy'],
                                     'cousins'       : [],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})

    transform_dict.update({'lgnr' : {'parents'       : ['lgnr', 'sgn3'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : ['lgn2'],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
  
    transform_dict.update({'lgn2' : {'parents'       : ['lgn2'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['qbt5'],
                                     'friends'       : []}})
    
    transform_dict.update({'sgn1' : {'parents'       : ['sgn1'],
                                     'siblings'      : [],
                                     'auntsuncles'   : [],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : ['sgn2'],
                                     'friends'       : []}})
    
    transform_dict.update({'qbt5' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['qbt5'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})
    
    transform_dict.update({'sgn2' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['sgn2'],
                                     'cousins'       : [NArw],
                                     'children'      : [],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})

    transform_dict.update({'sgn3' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['sgn3'],
                                     'cousins'       : [NArw],
                                     'children'      : ['sgn4'],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})

    transform_dict.update({'sgn4' : {'parents'       : [],
                                     'siblings'      : [],
                                     'auntsuncles'   : ['sgn4'],
                                     'cousins'       : [NArw],
                                     'children'      : ['sgn1'],
                                     'niecesnephews' : [],
                                     'coworkers'     : [],
                                     'friends'       : []}})

    return transform_dict
```

## Category processdict Entries

```
  def _assembleprocessdict(self):
    '''
    #creates a dictionary storing all of the processing functions for each
    #category. Note that the convention is that every dualprocess entry 
    #(to process both train and test data in automunge) is meant
    #to have a corresponding postprocess entry (to process the test set in 
    #postmunge). If the dualprocess/postprocess pair aren't included a 
    #singleprocess function should be instead which processes a single column
    #at a time and is neutral to whether that set is from train or test data.
      
    #note that the functionpointer entry is currently only available for user passed processdict
    #this internal library process_dict does not accept functionpointer entries
      
    #A user should pass either a pair of processing functions to both 
    #dualprocess and postprocess, or alternatively just a single processing
    #function to singleprocess, and omit or pass None to those not used.
    #A user can also pass an inversion function to inverseprocess if available.
    #Most of the transforms defined internal to the library follow this convention.
    
    #dualprocess: for passing a processing function in which normalization 
    #             parameters are derived from properties of the training set
    #             and jointly process the train set and if available corresponding test set
    
    #singleprocess: for passing a processing function in which no normalization
    #               parameters are needed from the train set to process the
    #               test set, such that train and test sets processed separately
    
    #postprocess: for passing a processing function in which normalization 
    #             parameters originally derived from the train set are applied
    #             to separately process a corresponding test set
    #             An entry should correspond to the dualprocess entry.

    #inverseprocess: for passing a processing function used to invert
    #                a corresponding forward pass transform
    #                An entry should correspond to the dualprocess or singleprocess entry.

    #__________________________________________________________________________
    #Alternative streamlined processing function conventions are also available 
    #which may be populated as entries to custom_train / custom_test / custom_inversion.
    #These conventions are documented in the readme section "Custom Transformation Functions".
    #In cases of redundancy custom_train entry specifications take precedence 
    #over dualprocess/singleprocess/postprocess entries.

    #custom_train: for passing a train set processing function in which normalization parameters
    #              are derived from properties of the training set. Will be used to process both 
    #              train and test data when custom_test not provided (in which case similar to singleprocess convention).

    #custom_test: for passing a test set processing function in which normalization parameters
    #             that were derived from properties of the training set are used to process the test data.
    #             When omitted custom_train will be used to process both the train and test data.
    #             An entry should correspond to the custom_train entry.

    #custom_inversion: for passing a processing function used to invert
    #                  a corresponding forward pass transform
    #                  An entry should correspond to the custom_train entry.

    #___________________________________________________________________________
    #The processdict also specifies various properties associated with the transformations. 
    #At a minimum, a user needs to specify NArowtype and MLinfilltype or otherwise
    #include a functionpointer entry.

    #___________________________________________________________________________
    #NArowtype: classifies the type of entries that are targets for infill.
    #           can be entries of {'numeric', 'integer', 'justNaN', 'exclude', 
    #                              'positivenumeric', 'nonnegativenumeric', 
    #                              'nonzeronumeric', 'parsenumeric', 'datetime'}
    #           Note that in the custom_train convention this is used to apply data type casting prior to the transform.
    # - 'numeric' for source columns with expected numeric entries
    # - 'integer' for source columns with expected integer entries
    # - 'justNaN' for source columns that may have expected entries other than numeric
    # - 'exclude' for source columns that aren't needing NArow columns derived
    # - 'positivenumeric' for source columns with expected positive numeric entries
    # - 'nonnegativenumeric' for source columns with expected non-negative numeric (zero allowed)
    # - 'nonzeronumeric' for source columns with allowed positive and negative but no zero
    # - 'parsenumeric' marks for infill strings that don't contain any numeric characters
    # - 'datetime' marks for infill cells that aren't recognized as datetime objects

    # ** Note that NArowtype also is used as basis for metrics evaluated in drift assessment of source columns
    # ** Note that by default any np.inf values are converted to NaN for infill
    # ** Note that by default python None entries are treated as targets for infill

    #___________________________________________________________________________
    #MLinfilltype: classifies data types of the returned set, 
    #              as may determine what types of models are trained for ML infill
    #              can be entries {'numeric', 'singlct', 'binary', 'multirt', 'concurrent_act', 'concurrent_nmbr', 
    #                              '1010', 'exclude', 'boolexclude', 'ordlexclude', 'totalexclude'}
    #              'numeric' single columns with numeric entries for regression (signed floats)
    #              'singlct' for single column sets with ordinal entries (nonnegative integer classification)
    #              'integer' for single column sets with integer entries (signed integer regression)
    #              'binary'  single column sets with boolean entries (0/1)
    #              'multirt' categoric multicolumn sets with boolean entries (0/1), up to one activation per row
    #              '1010'    for multicolumn sets with binary encoding via 1010, boolean integer entries (0/1), 
    #                        with distinct encoding representations by the set of activations
    #              'concurrent_act' for multicolumn sets with boolean integer entries as may have 
    #                               multiple entries in the same row, different from 1010 
    #                               in that columns are independent
    #              'concurrent_nmbr' for multicolumn sets with numeric entries (signed floats)
    #              'exclude' for columns which will be excluded from infill, 
    #                        returned data might not be numerically encoded
    #              'boolexclude' boolean set suitable for Binary transform but excluded from all infill 
    #                            (e.g. NArw entries)
    #              'ordlexclude' ordinal set exluded from infill (note that in some cases in library 
    #                            ordlexclude may return a multi-column set)
    #              'totalexclude' for complete passthroughs (excl) without datatype conversions, infill, 
    #                             and excluded from inf conversion and assignnan global option

    #___________________________________________________________________________
    #Other optional entries for processdict include:
    #info_retention, inplace_option, defaultparams, labelctgy, 
    #defaultinfill, dtype_convert, and functionpointer.

    #___________________________________________________________________________
    #info_retention: boolean marker associated with an inversion operation that helps inverison prioritize
    #transformation paths with full information recovery. (May pass as True when there is no information loss.)

    #___________________________________________________________________________
    #inplace_option: boolean marker indicating whether a transform supports the inplace parameter recieved in params.
    #                When not specified this is assumed as True (which is always valid for the custom_train convention).
    #                In other words, in dualprocess/singleprocess convention, if your transform does not support inplace,
    #                need to specify inplace_option as False

    #___________________________________________________________________________
    #defaultparams: a dictionary recording any default assignparam assignments associated with the category. 
    #               Note that deviations in user specifications to assignparam as part of an automunge(.) call
    #               take precedence over defaultparams. Note that when applying functionpointer defaultparams
    #               from the pointer target are also populated when not previously specified.

    #___________________________________________________________________________
    #defaultinfill: this option is specific to the custom_train convention, and serves to specify a default infill
    #               applied after NArowtype data type casting and preceding the transformation function.
    #               (defaultinfill is a precursor to ML infill or other infills applied based on assigninfill)
    #               defaults to 'adjinfill' when not specified, can also pass as one of
    #               {'adjinfill', 'meaninfill', 'medianinfill', 'modeinfill', 'lcinfill', 
    #                'zeroinfill', 'oneinfill', 'naninfill'}
    #               Note that 'meaninfill' and 'medianinfill' only work with numeric data (based on NArowtype).
    #               Note that for 'datetime' NArowtype, defaultinfill only supports 'adjinfill' or 'naninfill'
    #               Note that 'naninfill' is intended for cases where user wishes to apply their own default infill 
    #               as part of a custom_train entry

    #___________________________________________________________________________
    #dtype_convert: this option is intended for the custom_train convention, aceepts boolean entries,
    #               defaults to True when not specified, False turns off a data type conversion
    #               that is applied after custom_train transformation functions based on MLinfilltype.
    #               May also be used to deactivate a floatprecision conversion for any category. 
    #               This option primarily included to support special cases and not intended for wide use.

    #___________________________________________________________________________
    #labelctgy: an optional entry, should be a string entry of a single transformation category 
    #           as entered in the family tree when the category of the processdict entry is used as a root category. 
    #           Used to determine a basis of feature selection for cases where root 
    #           category is applied to a label set resulting in a set returned in multiple configurations. 
    #           Also used in label frequency levelizer. 
    #           Note that since this is only used for small edge case populating a labelctgy entry is optional. 
    #           If one is not assigned or accessed based on functionpointer, an arbitrary entry will be accessed 
    #           from the family tree. This option primarily included to support special cases.

    #___________________________________________________________________________
    #functionpointer: Only supported in user passed processdict, a functionpointer entry 
    #                 may be entered in lieu of any or all of these other entries **.
    #                 The functionpointer should be populated with a category that has its own processdict entry 
    #                 (or a category that has its own process_dict entry internal to the library)
    #                 The functionpointer inspects the pointer target and passes those specifications 
    #                 to the origin processdict entry unless previously specified.
    #                 The functionpointer is intended as a shortcut for specifying processdict entries
    #                 that may be helpful in cases where a new entry is very similar to some existing entry.
    #                 (**As the exception labelctgy not accessed from functionpointer 
    #                 since it is specific to a root category's family tree.)

    #___________________________________________________________________________
    #Other clarifications:
    #Note that NArowtype is associated with a category's use as a root category, 
    #and also for a category's use as a tree category in the custom_train convention
    #MLinfilltype is associated with a category's use as a tree category
    '''
    
    process_dict = {}
    
    #categories are nmbr, bnry, text, date, bxcx, bins, bint, NArw, null
    #note a future extension will allow the definition of new categories 
    #to automunge

    #dual column functions
    process_dict.update({'nmbr' : {'dualprocess' : self._process_numerical,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_numerical,
                                  'inverseprocess' : self._inverseprocess_nmbr,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'nmbr'}})
    process_dict.update({'dxdt' : {'dualprocess' : None,
                                  'singleprocess' : self._process_dxdt,
                                  'postprocess' : None,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'retn'}})
    process_dict.update({'d2dt' : {'dualprocess' : None,
                                  'singleprocess' : self._process_dxdt,
                                  'postprocess' : None,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'retn'}})
    process_dict.update({'d3dt' : {'dualprocess' : None,
                                  'singleprocess' : self._process_dxdt,
                                  'postprocess' : None,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'retn'}})
    process_dict.update({'d4dt' : {'dualprocess' : None,
                                  'singleprocess' : self._process_dxdt,
                                  'postprocess' : None,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'retn'}})
    process_dict.update({'d5dt' : {'dualprocess' : None,
                                  'singleprocess' : self._process_dxdt,
                                  'postprocess' : None,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'retn'}})
    process_dict.update({'d6dt' : {'dualprocess' : None,
                                  'singleprocess' : self._process_dxdt,
                                  'postprocess' : None,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'retn'}})
    process_dict.update({'dxd2' : {'dualprocess' : None,
                                  'singleprocess' : self._process_dxd2,
                                  'postprocess' : None,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'retn'}})
    process_dict.update({'d2d2' : {'dualprocess' : None,
                                  'singleprocess' : self._process_dxd2,
                                  'postprocess' : None,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'retn'}})
    process_dict.update({'d3d2' : {'dualprocess' : None,
                                  'singleprocess' : self._process_dxd2,
                                  'postprocess' : None,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'retn'}})
    process_dict.update({'d4d2' : {'dualprocess' : None,
                                  'singleprocess' : self._process_dxd2,
                                  'postprocess' : None,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'retn'}})
    process_dict.update({'d5d2' : {'dualprocess' : None,
                                  'singleprocess' : self._process_dxd2,
                                  'postprocess' : None,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'retn'}})
    process_dict.update({'d6d2' : {'dualprocess' : None,
                                  'singleprocess' : self._process_dxd2,
                                  'postprocess' : None,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'retn'}})
    process_dict.update({'nmdx' : {'dualprocess' : self._process_numerical,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_numerical,
                                  'inverseprocess' : self._inverseprocess_nmbr,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'retn'}})
    process_dict.update({'nmd2' : {'dualprocess' : self._process_numerical,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_numerical,
                                  'inverseprocess' : self._inverseprocess_nmbr,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'retn'}})
    process_dict.update({'nmd3' : {'dualprocess' : self._process_numerical,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_numerical,
                                  'inverseprocess' : self._inverseprocess_nmbr,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'retn'}})
    process_dict.update({'nmd4' : {'dualprocess' : self._process_numerical,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_numerical,
                                  'inverseprocess' : self._inverseprocess_nmbr,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'retn'}})
    process_dict.update({'nmd5' : {'dualprocess' : self._process_numerical,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_numerical,
                                  'inverseprocess' : self._inverseprocess_nmbr,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'retn'}})
    process_dict.update({'nmd6' : {'dualprocess' : self._process_numerical,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_numerical,
                                  'inverseprocess' : self._inverseprocess_nmbr,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'retn'}})
    process_dict.update({'mmdx' : {'dualprocess' : None,
                                  'singleprocess' : self._process_dxdt,
                                  'postprocess' : None,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'nmbr'}})
    process_dict.update({'mmd2' : {'dualprocess' : None,
                                  'singleprocess' : self._process_dxdt,
                                  'postprocess' : None,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'nmbr'}})
    process_dict.update({'mmd3' : {'dualprocess' : None,
                                  'singleprocess' : self._process_dxdt,
                                  'postprocess' : None,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'nmbr'}})
    process_dict.update({'mmd4' : {'dualprocess' : None,
                                  'singleprocess' : self._process_dxdt,
                                  'postprocess' : None,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'nmbr'}})
    process_dict.update({'mmd5' : {'dualprocess' : None,
                                  'singleprocess' : self._process_dxdt,
                                  'postprocess' : None,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'nmbr'}})
    process_dict.update({'mmd6' : {'dualprocess' : None,
                                  'singleprocess' : self._process_dxdt,
                                  'postprocess' : None,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'nmbr'}})
    process_dict.update({'dddt' : {'dualprocess' : None,
                                  'singleprocess' : self._process_dxdt,
                                  'postprocess' : None,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'dddt'}})
    process_dict.update({'ddd2' : {'dualprocess' : None,
                                  'singleprocess' : self._process_dxdt,
                                  'postprocess' : None,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'dddt'}})
    process_dict.update({'ddd3' : {'dualprocess' : None,
                                  'singleprocess' : self._process_dxdt,
                                  'postprocess' : None,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'dddt'}})
    process_dict.update({'ddd4' : {'dualprocess' : None,
                                  'singleprocess' : self._process_dxdt,
                                  'postprocess' : None,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'dddt'}})
    process_dict.update({'ddd5' : {'dualprocess' : None,
                                  'singleprocess' : self._process_dxdt,
                                  'postprocess' : None,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'dddt'}})
    process_dict.update({'ddd6' : {'dualprocess' : None,
                                  'singleprocess' : self._process_dxdt,
                                  'postprocess' : None,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'dddt'}})
    process_dict.update({'dedt' : {'dualprocess' : None,
                                  'singleprocess' : self._process_dxd2,
                                  'postprocess' : None,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'dedt'}})
    process_dict.update({'ded2' : {'dualprocess' : None,
                                  'singleprocess' : self._process_dxd2,
                                  'postprocess' : None,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'dedt'}})
    process_dict.update({'ded3' : {'dualprocess' : None,
                                  'singleprocess' : self._process_dxd2,
                                  'postprocess' : None,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'dedt'}})
    process_dict.update({'ded4' : {'dualprocess' : None,
                                  'singleprocess' : self._process_dxd2,
                                  'postprocess' : None,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'dedt'}})
    process_dict.update({'ded5' : {'dualprocess' : None,
                                  'singleprocess' : self._process_dxd2,
                                  'postprocess' : None,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'dedt'}})
    process_dict.update({'ded6' : {'dualprocess' : None,
                                  'singleprocess' : self._process_dxd2,
                                  'postprocess' : None,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'dedt'}})
    process_dict.update({'shft' : {'dualprocess' : None,
                                  'singleprocess' : self._process_shft,
                                  'postprocess' : None,
                                  'inverseprocess' : self._inverseprocess_shft,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'defaultparams' : {'periods' : 1},
                                  'NArowtype' : 'exclude',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'shft'}})
    process_dict.update({'shf2' : {'dualprocess' : None,
                                  'singleprocess' : self._process_shft,
                                  'postprocess' : None,
                                  'inverseprocess' : self._inverseprocess_shft,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'defaultparams' : {'periods' : 2},
                                  'NArowtype' : 'exclude',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'shf2'}})
    process_dict.update({'shf3' : {'dualprocess' : None,
                                  'singleprocess' : self._process_shft,
                                  'postprocess' : None,
                                  'inverseprocess' : self._inverseprocess_shft,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'defaultparams' : {'periods' : 3},
                                  'NArowtype' : 'exclude',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'shf3'}})
    process_dict.update({'shf4' : {'dualprocess' : None,
                                  'singleprocess' : self._process_shft,
                                  'postprocess' : None,
                                  'inverseprocess' : self._inverseprocess_shft,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'defaultparams' : {'periods' : 1},
                                  'NArowtype' : 'exclude',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'retn'}})
    process_dict.update({'shf5' : {'dualprocess' : None,
                                  'singleprocess' : self._process_shft,
                                  'postprocess' : None,
                                  'inverseprocess' : self._inverseprocess_shft,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'defaultparams' : {'periods' : 2},
                                  'NArowtype' : 'exclude',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'retn'}})
    process_dict.update({'shf6' : {'dualprocess' : None,
                                  'singleprocess' : self._process_shft,
                                  'postprocess' : None,
                                  'inverseprocess' : self._inverseprocess_shft,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'defaultparams' : {'periods' : 3},
                                  'NArowtype' : 'exclude',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'retn'}})
    process_dict.update({'shf7' : {'dualprocess' : None,
                                  'singleprocess' : self._process_shft,
                                  'postprocess' : None,
                                  'inverseprocess' : self._inverseprocess_shft,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'exclude',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'retn'}})
    process_dict.update({'shf8' : {'dualprocess' : None,
                                  'singleprocess' : self._process_shft,
                                  'postprocess' : None,
                                  'inverseprocess' : self._inverseprocess_shft,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'exclude',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'retn'}})
    process_dict.update({'nbr2' : {'dualprocess' : self._process_numerical,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_numerical,
                                  'inverseprocess' : self._inverseprocess_nmbr,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'nmbr'}})
    process_dict.update({'nbr3' : {'dualprocess' : self._process_numerical,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_numerical,
                                  'inverseprocess' : self._inverseprocess_nmbr,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'nbr3'}})
    process_dict.update({'MADn' : {'dualprocess' : self._process_MADn,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_MADn,
                                  'inverseprocess' : self._inverseprocess_MADn,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'defaultparams' : {'center' : 'mean'},
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'MADn'}})
    process_dict.update({'MAD2' : {'dualprocess' : self._process_MADn,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_MADn,
                                  'inverseprocess' : self._inverseprocess_MADn,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'defaultparams' : {'center' : 'mean'},
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'MAD2'}})
    process_dict.update({'MAD3' : {'dualprocess' : self._process_MADn,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_MADn,
                                  'inverseprocess' : self._inverseprocess_MADn,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'defaultparams' : {'center' : 'max'},
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'MAD3'}})
    process_dict.update({'mnmx' : {'dualprocess' : self._process_mnmx,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_mnmx,
                                  'inverseprocess' : self._inverseprocess_mnmx,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'mnmx'}})
    process_dict.update({'mnm2' : {'dualprocess' : self._process_mnmx,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_mnmx,
                                  'inverseprocess' : self._inverseprocess_mnmx,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'mnmx'}})
    process_dict.update({'mnm3' : {'dualprocess' : self._process_mnm3,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_mnm3,
                                  'inverseprocess' : self._inverseprocess_mnm3,
                                  'info_retention' : False,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'mnm3'}})
    process_dict.update({'mnm4' : {'dualprocess' : self._process_mnm3,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_mnm3,
                                  'inverseprocess' : self._inverseprocess_mnm3,
                                  'info_retention' : False,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'mnm3'}})
    process_dict.update({'mnm5' : {'dualprocess' : self._process_mnmx,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_mnmx,
                                  'inverseprocess' : self._inverseprocess_mnmx,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'mnmx'}})
    process_dict.update({'mnm6' : {'dualprocess' : self._process_mnmx,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_mnmx,
                                  'inverseprocess' : self._inverseprocess_mnmx,
                                  'defaultparams' : {'floor' : True},
                                  'info_retention' : False,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'mnm6'}})
    process_dict.update({'mnm7' : {'dualprocess' : None,
                                  'singleprocess' : None,
                                  'postprocess' : None,
                                  'inplace_option' : False,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'mnmx'}})
    process_dict.update({'mxab' : {'dualprocess' : self._process_mxab,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_mxab,
                                  'inverseprocess' : self._inverseprocess_mxab,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'mxab'}})
    process_dict.update({'retn' : {'dualprocess' : self._process_retn,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_retn,
                                  'inverseprocess' : self._inverseprocess_retn,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'retn'}})
    process_dict.update({'rtbn' : {'dualprocess' : self._process_retn,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_retn,
                                  'inverseprocess' : self._inverseprocess_retn,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'retn'}})
    process_dict.update({'rtb2' : {'dualprocess' : self._process_retn,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_retn,
                                  'inverseprocess' : self._inverseprocess_retn,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'retn'}})
    process_dict.update({'mean' : {'dualprocess' : self._process_mean,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_mean,
                                  'inverseprocess' : self._inverseprocess_mean,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'mean'}})
    process_dict.update({'mea2' : {'dualprocess' : self._process_mean,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_mean,
                                  'inverseprocess' : self._inverseprocess_mean,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'mean'}})
    process_dict.update({'mea3' : {'dualprocess' : self._process_mean,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_mean,
                                  'inverseprocess' : self._inverseprocess_mean,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'mean'}})
    process_dict.update({'bnry' : {'dualprocess' : self._process_binary,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_binary,
                                  'inverseprocess' : self._inverseprocess_bnry,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'defaultparams' : {'infillconvention' : 'onevalue'},
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'binary',
                                  'labelctgy' : 'bnry'}})
    process_dict.update({'bnr2' : {'dualprocess' : self._process_binary,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_binary,
                                  'inverseprocess' : self._inverseprocess_bnry,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'defaultparams' : {'infillconvention' : 'zerovalue'},
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'binary',
                                  'labelctgy' : 'bnr2'}})
    process_dict.update({'onht' : {'dualprocess' : self._process_onht,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_onht,
                                  'inverseprocess' : self._inverseprocess_onht,
                                  'info_retention' : True,
                                  'inplace_option' : False,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'multirt',
                                  'labelctgy' : 'onht'}})
    process_dict.update({'text' : {'dualprocess' : self._process_text,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_text,
                                  'inverseprocess' : self._inverseprocess_text,
                                  'info_retention' : True,
                                  'inplace_option' : False,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'multirt',
                                  'labelctgy' : 'text'}})
    process_dict.update({'txt2' : {'dualprocess' : self._process_text,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_text,
                                  'inverseprocess' : self._inverseprocess_text,
                                  'info_retention' : True,
                                  'inplace_option' : False,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'multirt',
                                  'labelctgy' : 'text'}})
    process_dict.update({'txt3' : {'dualprocess' : self._process_spl2,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_spl2,
                                  'inverseprocess' : self._inverseprocess_spl2,
                                  'info_retention' : False,
                                  'inplace_option' : False,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'exclude',
                                  'labelctgy' : 'text'}})
    process_dict.update({'smth' : {'dualprocess' : self._process_smth,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_smth,
                                  'inverseprocess' : self._inverseprocess_smth,
                                  'info_retention' : True,
                                  'inplace_option' : False,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'exclude',
                                  'labelctgy' : 'smth'}})
    process_dict.update({'fsmh' : {'dualprocess' : self._process_smth,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_smth,
                                  'inverseprocess' : self._inverseprocess_smth,
                                  'info_retention' : True,
                                  'inplace_option' : False,
                                  'defaultparams' : {'LSfit' : True},
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'exclude',
                                  'labelctgy' : 'fsmh'}})
    process_dict.update({'lngt' : {'dualprocess' : None,
                                  'singleprocess' : self._process_lngt,
                                  'postprocess' : None,
                                  'inplace_option' : False,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'integer',
                                  'labelctgy' : 'mnmx'}})
    process_dict.update({'lnlg' : {'dualprocess' : None,
                                  'singleprocess' : self._process_lngt,
                                  'postprocess' : None,
                                  'inplace_option' : False,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'integer',
                                  'labelctgy' : 'log0'}})
    process_dict.update({'UPCS' : {'dualprocess' : None,
                                  'singleprocess' : self._process_UPCS,
                                  'postprocess' : None,
                                  'inverseprocess' : self._inverseprocess_UPCS,
                                  'info_retention' : False,
                                  'inplace_option' : True,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'exclude',
                                  'labelctgy' : 'UPCS'}})
    process_dict.update({'Unht' : {'dualprocess' : None,
                                  'singleprocess' : self._process_UPCS,
                                  'postprocess' : None,
                                  'inverseprocess' : self._inverseprocess_UPCS,
                                  'info_retention' : False,
                                  'inplace_option' : True,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'exclude',
                                  'labelctgy' : 'onht'}})
    process_dict.update({'Utxt' : {'dualprocess' : None,
                                  'singleprocess' : self._process_UPCS,
                                  'postprocess' : None,
                                  'inverseprocess' : self._inverseprocess_UPCS,
                                  'info_retention' : False,
                                  'inplace_option' : True,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'exclude',
                                  'labelctgy' : 'text'}})
    process_dict.update({'Utx2' : {'dualprocess' : None,
                                  'singleprocess' : self._process_UPCS,
                                  'postprocess' : None,
                                  'inverseprocess' : self._inverseprocess_UPCS,
                                  'info_retention' : False,
                                  'inplace_option' : True,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'exclude',
                                  'labelctgy' : 'text'}})
    process_dict.update({'Utx3' : {'dualprocess' : None,
                                  'singleprocess' : self._process_UPCS,
                                  'postprocess' : None,
                                  'inverseprocess' : self._inverseprocess_UPCS,
                                  'info_retention' : False,
                                  'inplace_option' : True,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'exclude',
                                  'labelctgy' : 'text'}})
    process_dict.update({'Ucct' : {'dualprocess' : None,
                                  'singleprocess' : self._process_UPCS,
                                  'postprocess' : None,
                                  'inverseprocess' : self._inverseprocess_UPCS,
                                  'info_retention' : False,
                                  'inplace_option' : True,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'exclude',
                                  'labelctgy' : 'ord3'}})
    process_dict.update({'Uord' : {'dualprocess' : None,
                                  'singleprocess' : self._process_UPCS,
                                  'postprocess' : None,
                                  'inverseprocess' : self._inverseprocess_UPCS,
                                  'info_retention' : False,
                                  'inplace_option' : True,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'exclude',
                                  'labelctgy' : 'ordl'}})
    process_dict.update({'Uor2' : {'dualprocess' : None,
                                  'singleprocess' : self._process_UPCS,
                                  'postprocess' : None,
                                  'inverseprocess' : self._inverseprocess_UPCS,
                                  'info_retention' : False,
                                  'inplace_option' : True,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'exclude',
                                  'labelctgy' : 'mnmx'}})
    process_dict.update({'Uor3' : {'dualprocess' : None,
                                  'singleprocess' : self._process_UPCS,
                                  'postprocess' : None,
                                  'inverseprocess' : self._inverseprocess_UPCS,
                                  'info_retention' : False,
                                  'inplace_option' : True,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'exclude',
                                  'labelctgy' : 'ord3'}})
    process_dict.update({'Uor6' : {'dualprocess' : None,
                                  'singleprocess' : self._process_UPCS,
                                  'postprocess' : None,
                                  'inverseprocess' : self._inverseprocess_UPCS,
                                  'info_retention' : False,
                                  'inplace_option' : True,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'exclude',
                                  'labelctgy' : 'ord3'}})
    process_dict.update({'U101' : {'dualprocess' : None,
                                  'singleprocess' : self._process_UPCS,
                                  'postprocess' : None,
                                  'inverseprocess' : self._inverseprocess_UPCS,
                                  'info_retention' : False,
                                  'inplace_option' : True,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'exclude',
                                  'labelctgy' : '1010'}})
    process_dict.update({'splt' : {'dualprocess' : self._process_splt,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_splt,
                                  'inverseprocess' : self._inverseprocess_splt,
                                  'info_retention' : False,
                                  'inplace_option' : False,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'multirt',
                                  'labelctgy' : 'splt'}})
    process_dict.update({'spl2' : {'dualprocess' : self._process_spl2,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_spl2,
                                  'inverseprocess' : self._inverseprocess_spl2,
                                  'info_retention' : False,
                                  'inplace_option' : False,
                                  'defaultparams' : {'test_same_as_train' : False,
                                                     'consolidate_nonoverlaps' : False},
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'exclude',
                                  'labelctgy' : 'ord3'}})
    process_dict.update({'spl5' : {'dualprocess' : self._process_spl2,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_spl2,
                                  'inverseprocess' : self._inverseprocess_spl2,
                                  'info_retention' : False,
                                  'inplace_option' : False,
                                  'defaultparams' : {'test_same_as_train' : False,
                                                     'consolidate_nonoverlaps' : True},
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'exclude',
                                  'labelctgy' : 'ord3'}})
    process_dict.update({'spl6' : {'dualprocess' : self._process_spl2,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_spl2,
                                  'inverseprocess' : self._inverseprocess_spl2,
                                  'info_retention' : False,
                                  'inplace_option' : False,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'exclude',
                                  'labelctgy' : 'ord3'}})
    process_dict.update({'spl7' : {'dualprocess' : self._process_spl2,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_spl2,
                                  'inverseprocess' : self._inverseprocess_spl2,
                                  'info_retention' : False,
                                  'inplace_option' : False,
                                  'defaultparams' : {'test_same_as_train' : False,
                                                     'consolidate_nonoverlaps' : True,
                                                     'minsplit' : 1},
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'exclude',
                                  'labelctgy' : 'ord3'}})
    process_dict.update({'spl8' : {'dualprocess' : self._process_splt,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_splt,
                                  'inverseprocess' : self._inverseprocess_splt,
                                  'info_retention' : False,
                                  'inplace_option' : False,
                                  'defaultparams' : {'test_same_as_train' : True},
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'multirt',
                                  'labelctgy' : 'spl8'}})
    process_dict.update({'spl9' : {'dualprocess' : self._process_spl2,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_spl2,
                                  'inverseprocess' : self._inverseprocess_spl2,
                                  'info_retention' : False,
                                  'inplace_option' : False,
                                  'defaultparams' : {'test_same_as_train' : True,
                                                     'consolidate_nonoverlaps' : False},
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'exclude',
                                  'labelctgy' : 'ord3'}})
    process_dict.update({'sp10' : {'dualprocess' : self._process_spl2,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_spl2,
                                  'inverseprocess' : self._inverseprocess_spl2,
                                  'info_retention' : False,
                                  'inplace_option' : False,
                                  'defaultparams' : {'test_same_as_train' : True,
                                                     'consolidate_nonoverlaps' : True},
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'exclude',
                                  'labelctgy' : 'ord3'}})
    process_dict.update({'sp11' : {'dualprocess' : self._process_spl2,
                                   'singleprocess' : None,
                                   'postprocess' : self._postprocess_spl2,
                                   'inverseprocess' : self._inverseprocess_spl2,
                                   'info_retention' : False,
                                   'inplace_option' : False,
                                   'defaultparams' : {'test_same_as_train' : False,
                                                      'consolidate_nonoverlaps' : False},
                                   'NArowtype' : 'justNaN',
                                   'MLinfilltype' : 'exclude',
                                   'labelctgy' : 'ord3'}})
    process_dict.update({'sp12' : {'dualprocess' : self._process_spl2,
                                   'singleprocess' : None,
                                   'postprocess' : self._postprocess_spl2,
                                   'inverseprocess' : self._inverseprocess_spl2,
                                   'info_retention' : False,
                                   'inplace_option' : False,
                                   'defaultparams' : {'test_same_as_train' : False,
                                                      'consolidate_nonoverlaps' : False},
                                   'NArowtype' : 'justNaN',
                                   'MLinfilltype' : 'exclude',
                                   'labelctgy' : 'ord3'}})
    process_dict.update({'sp13' : {'dualprocess' : self._process_spl2,
                                   'singleprocess' : None,
                                   'postprocess' : self._postprocess_spl2,
                                   'inverseprocess' : self._inverseprocess_spl2,
                                   'info_retention' : False,
                                   'inplace_option' : False,
                                   'defaultparams' : {'test_same_as_train' : True,
                                                      'consolidate_nonoverlaps' : False},
                                   'NArowtype' : 'justNaN',
                                   'MLinfilltype' : 'exclude',
                                   'labelctgy' : 'ord3'}})
    process_dict.update({'sp14' : {'dualprocess' : self._process_spl2,
                                   'singleprocess' : None,
                                   'postprocess' : self._postprocess_spl2,
                                   'inverseprocess' : self._inverseprocess_spl2,
                                   'info_retention' : False,
                                   'inplace_option' : False,
                                   'defaultparams' : {'test_same_as_train' : True,
                                                      'consolidate_nonoverlaps' : False},
                                   'NArowtype' : 'justNaN',
                                   'MLinfilltype' : 'exclude',
                                   'labelctgy' : 'ord3'}})
    process_dict.update({'sp15' : {'dualprocess' : self._process_splt,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_splt,
                                  'inverseprocess' : self._inverseprocess_splt,
                                  'info_retention' : False,
                                  'inplace_option' : False,
                                  'defaultparams' : {'concurrent_activations': True,
                                                     'test_same_as_train' : False},
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'concurrent_act',
                                  'labelctgy' : 'sp15'}})
    process_dict.update({'sp16' : {'dualprocess' : self._process_splt,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_splt,
                                  'inverseprocess' : self._inverseprocess_splt,
                                  'info_retention' : False,
                                  'inplace_option' : False,
                                  'defaultparams' : {'concurrent_activations': True,
                                                     'test_same_as_train' : True},
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'concurrent_act',
                                  'labelctgy' : 'sp16'}})
    process_dict.update({'sp17' : {'dualprocess' : self._process_spl2,
                                   'singleprocess' : None,
                                   'postprocess' : self._postprocess_spl2,
                                   'inverseprocess' : self._inverseprocess_spl2,
                                   'info_retention' : False,
                                   'inplace_option' : False,
                                   'defaultparams' : {'test_same_as_train' : False,
                                                      'consolidate_nonoverlaps' : False},
                                   'NArowtype' : 'justNaN',
                                   'MLinfilltype' : 'exclude',
                                   'labelctgy' : 'ord3'}})
    process_dict.update({'sp18' : {'dualprocess' : self._process_spl2,
                                   'singleprocess' : None,
                                   'postprocess' : self._postprocess_spl2,
                                   'inverseprocess' : self._inverseprocess_spl2,
                                   'info_retention' : False,
                                   'inplace_option' : False,
                                   'defaultparams' : {'test_same_as_train' : False,
                                                      'consolidate_nonoverlaps' : False},
                                   'NArowtype' : 'justNaN',
                                   'MLinfilltype' : 'exclude',
                                   'labelctgy' : 'ord3'}})
    process_dict.update({'sp19' : {'dualprocess' : self._process_sp19,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_sp19,
                                  'inverseprocess' : self._inverseprocess_sp19,
                                  'info_retention' : False,
                                  'inplace_option' : False,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : '1010',
                                  'labelctgy' : 'sp19'}})
    process_dict.update({'sp20' : {'dualprocess' : self._process_sp19,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_sp19,
                                  'inverseprocess' : self._inverseprocess_sp19,
                                  'info_retention' : False,
                                  'inplace_option' : False,
                                  'defaultparams' : {'test_same_as_train' : True},
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : '1010',
                                  'labelctgy' : 'sp20'}})
    process_dict.update({'sbst' : {'dualprocess' : self._process_sbst,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_sbst,
                                  'inverseprocess' : self._inverseprocess_sbst,
                                  'info_retention' : False,
                                  'inplace_option' : False,
                                  'defaultparams' : {'test_same_as_train' : False},
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'concurrent_act',
                                  'labelctgy' : 'sbst'}})
    process_dict.update({'sbs2' : {'dualprocess' : self._process_sbst,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_sbst,
                                  'inverseprocess' : self._inverseprocess_sbst,
                                  'info_retention' : False,
                                  'inplace_option' : False,
                                  'defaultparams' : {'test_same_as_train' : True},
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'concurrent_act',
                                  'labelctgy' : 'sbs2'}})
    process_dict.update({'sbs3' : {'dualprocess' : self._process_sbs3,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_sbs3,
                                  'inverseprocess' : self._inverseprocess_sbs3,
                                  'info_retention' : False,
                                  'inplace_option' : False,
                                  'defaultparams' : {'test_same_as_train' : False},
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : '1010',
                                  'labelctgy' : 'sbs3'}})
    process_dict.update({'sbs4' : {'dualprocess' : self._process_sbs3,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_sbs3,
                                  'inverseprocess' : self._inverseprocess_sbs3,
                                  'info_retention' : False,
                                  'inplace_option' : False,
                                  'defaultparams' : {'test_same_as_train' : True},
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : '1010',
                                  'labelctgy' : 'sbs4'}})
    process_dict.update({'hash' : {'dualprocess' : self._process_hash,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_hash,
                                  'inplace_option' : True,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'ordlexclude',
                                  'labelctgy' : 'hash'}})
    process_dict.update({'hsh2' : {'dualprocess' : self._process_hash,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_hash,
                                  'inplace_option' : True,
                                  'defaultparams' : {'space' : '',
                                                     'excluded_characters' : []},
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'ordlexclude',
                                  'labelctgy' : 'hsh2'}})
    process_dict.update({'hs10' : {'dualprocess' : self._process_hs10,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_hs10,
                                  'inplace_option' : True,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'boolexclude',
                                  'labelctgy' : 'hs10'}})
    process_dict.update({'Uhsh' : {'dualprocess' : None,
                                  'singleprocess' : self._process_UPCS,
                                  'postprocess' : None,
                                  'inverseprocess' : self._inverseprocess_UPCS,
                                  'info_retention' : False,
                                  'inplace_option' : True,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'exclude',
                                  'labelctgy' : 'hash'}})
    process_dict.update({'Uhs2' : {'dualprocess' : None,
                                  'singleprocess' : self._process_UPCS,
                                  'postprocess' : None,
                                  'inverseprocess' : self._inverseprocess_UPCS,
                                  'info_retention' : False,
                                  'inplace_option' : True,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'exclude',
                                  'labelctgy' : 'hsh2'}})
    process_dict.update({'Uh10' : {'dualprocess' : None,
                                  'singleprocess' : self._process_UPCS,
                                  'postprocess' : None,
                                  'inverseprocess' : self._inverseprocess_UPCS,
                                  'info_retention' : False,
                                  'inplace_option' : True,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'exclude',
                                  'labelctgy' : 'hs10'}})
    process_dict.update({'srch' : {'dualprocess' : self._process_srch,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_srch,
                                  'inverseprocess' : self._inverseprocess_srch,
                                  'info_retention' : False,
                                  'inplace_option' : False,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'concurrent_act',
                                  'labelctgy' : 'srch'}})
    process_dict.update({'src2' : {'dualprocess' : self._process_src2,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_src2,
                                  'inverseprocess' : self._inverseprocess_src2,
                                  'info_retention' : False,
                                  'inplace_option' : False,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'concurrent_act',
                                  'labelctgy' : 'src2'}})
    process_dict.update({'src3' : {'dualprocess' : self._process_src3,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_src3,
                                  'inverseprocess' : self._inverseprocess_src3,
                                  'info_retention' : False,
                                  'inplace_option' : False,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'concurrent_act',
                                  'labelctgy' : 'src3'}})
    process_dict.update({'src4' : {'dualprocess' : self._process_src4,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_src4,
                                  'inverseprocess' : self._inverseprocess_src4,
                                  'info_retention' : False,
                                  'inplace_option' : False,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'singlct',
                                  'labelctgy' : 'src4'}})
    process_dict.update({'aggt' : {'dualprocess' : None,
                                  'singleprocess' : self._process_aggt,
                                  'postprocess' : None,
                                  'inverseprocess' : self._inverseprocess_UPCS,
                                  'info_retention' : False,
                                  'inplace_option' : False,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'exclude',
                                  'labelctgy' : 'ord3'}})
    process_dict.update({'strn' : {'dualprocess' : None,
                                  'singleprocess' : self._process_strn,
                                  'postprocess' : None,
                                  'inplace_option' : False,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'exclude',
                                  'labelctgy' : 'ord3'}})
    process_dict.update({'strg' : {'dualprocess' : None,
                                  'singleprocess' : self._process_strg,
                                  'postprocess' : None,
                                  'inverseprocess' : self._inverseprocess_strg,
                                  'info_retention' : True,
                                  'inplace_option' : False,
                                  'NArowtype' : 'integer',
                                  'MLinfilltype' : 'exclude',
                                  'labelctgy' : 'strg'}})
    process_dict.update({'nmrc' : {'dualprocess' : None,
                                  'singleprocess' : self._process_nmrc,
                                  'postprocess' : None,
                                  'inverseprocess' : self._inverseprocess_nmrc,
                                  'info_retention' : True,
                                  'inplace_option' : False,
                                  'defaultparams' : {'convention' : 'numbers'},
                                  'NArowtype' : 'parsenumeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'nmrc'}})
    process_dict.update({'nmr2' : {'dualprocess' : None,
                                  'singleprocess' : self._process_nmrc,
                                  'postprocess' : None,
                                  'inverseprocess' : self._inverseprocess_nmrc,
                                  'info_retention' : False,
                                  'inplace_option' : False,
                                  'defaultparams' : {'convention' : 'numbers'},
                                  'NArowtype' : 'parsenumeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'nmbr'}})
    process_dict.update({'nmr3' : {'dualprocess' : None,
                                  'singleprocess' : self._process_nmrc,
                                  'postprocess' : None,
                                  'inverseprocess' : self._inverseprocess_nmrc,
                                  'info_retention' : False,
                                  'inplace_option' : False,
                                  'defaultparams' : {'convention' : 'numbers'},
                                  'NArowtype' : 'parsenumeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'mnmx'}})
    process_dict.update({'nmr4' : {'dualprocess' : self._process_nmr4,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_nmr4,
                                  'inverseprocess' : self._inverseprocess_nmrc,
                                  'info_retention' : True,
                                  'inplace_option' : False,
                                  'defaultparams' : {'convention' : 'numbers',
                                                     'test_same_as_train' : True},
                                  'NArowtype' : 'parsenumeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'nmr4'}})
    process_dict.update({'nmr5' : {'dualprocess' : self._process_nmr4,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_nmr4,
                                  'inverseprocess' : self._inverseprocess_nmrc,
                                  'info_retention' : False,
                                  'inplace_option' : False,
                                  'defaultparams' : {'convention' : 'numbers',
                                                     'test_same_as_train' : True},
                                  'NArowtype' : 'parsenumeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'nmbr'}})
    process_dict.update({'nmr6' : {'dualprocess' : self._process_nmr4,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_nmr4,
                                  'inverseprocess' : self._inverseprocess_nmrc,
                                  'info_retention' : False,
                                  'inplace_option' : False,
                                  'defaultparams' : {'convention' : 'numbers',
                                                     'test_same_as_train' : True},
                                  'NArowtype' : 'parsenumeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'mnmx'}})
    process_dict.update({'nmr7' : {'dualprocess' : self._process_nmr4,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_nmr4,
                                  'inverseprocess' : self._inverseprocess_nmrc,
                                  'info_retention' : False,
                                  'inplace_option' : False,
                                  'defaultparams' : {'convention' : 'numbers',
                                                     'test_same_as_train' : False},
                                  'NArowtype' : 'parsenumeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'nmr7'}})
    process_dict.update({'nmr8' : {'dualprocess' : self._process_nmr4,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_nmr4,
                                  'inverseprocess' : self._inverseprocess_nmrc,
                                  'info_retention' : False,
                                  'inplace_option' : False,
                                  'defaultparams' : {'convention' : 'numbers',
                                                     'test_same_as_train' : False},
                                  'NArowtype' : 'parsenumeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'nmbr'}})
    process_dict.update({'nmr9' : {'dualprocess' : self._process_nmr4,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_nmr4,
                                  'inverseprocess' : self._inverseprocess_nmrc,
                                  'info_retention' : False,
                                  'inplace_option' : False,
                                  'defaultparams' : {'convention' : 'numbers',
                                                     'test_same_as_train' : False},
                                  'NArowtype' : 'parsenumeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'mnmx'}})
    process_dict.update({'nmcm' : {'dualprocess' : None,
                                  'singleprocess' : self._process_nmrc,
                                  'postprocess' : None,
                                  'inverseprocess' : self._inverseprocess_nmrc,
                                  'info_retention' : True,
                                  'inplace_option' : False,
                                  'defaultparams' : {'convention' : 'commas'},
                                  'NArowtype' : 'parsenumeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'nmcm'}})
    process_dict.update({'nmc2' : {'dualprocess' : None,
                                  'singleprocess' : self._process_nmrc,
                                  'postprocess' : None,
                                  'inverseprocess' : self._inverseprocess_nmrc,
                                  'info_retention' : False,
                                  'inplace_option' : False,
                                  'defaultparams' : {'convention' : 'commas'},
                                  'NArowtype' : 'parsenumeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'nmbr'}})
    process_dict.update({'nmc3' : {'dualprocess' : None,
                                  'singleprocess' : self._process_nmrc,
                                  'postprocess' : None,
                                  'inverseprocess' : self._inverseprocess_nmrc,
                                  'info_retention' : False,
                                  'inplace_option' : False,
                                  'defaultparams' : {'convention' : 'commas'},
                                  'NArowtype' : 'parsenumeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'mnmx'}})
    process_dict.update({'nmc4' : {'dualprocess' : self._process_nmr4,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_nmr4,
                                  'inverseprocess' : self._inverseprocess_nmrc,
                                  'info_retention' : True,
                                  'inplace_option' : False,
                                  'defaultparams' : {'convention' : 'commas',
                                                     'test_same_as_train' : True},
                                  'NArowtype' : 'parsenumeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'nmc4'}})
    process_dict.update({'nmc5' : {'dualprocess' : self._process_nmr4,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_nmr4,
                                  'inverseprocess' : self._inverseprocess_nmrc,
                                  'info_retention' : False,
                                  'inplace_option' : False,
                                  'defaultparams' : {'convention' : 'commas',
                                                     'test_same_as_train' : True},
                                  'NArowtype' : 'parsenumeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'nmbr'}})
    process_dict.update({'nmc6' : {'dualprocess' : self._process_nmr4,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_nmr4,
                                  'inverseprocess' : self._inverseprocess_nmrc,
                                  'info_retention' : False,
                                  'inplace_option' : False,
                                  'defaultparams' : {'convention' : 'commas',
                                                     'test_same_as_train' : True},
                                  'NArowtype' : 'parsenumeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'mnmx'}})
    process_dict.update({'nmc7' : {'dualprocess' : self._process_nmr4,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_nmr4,
                                  'inverseprocess' : self._inverseprocess_nmrc,
                                  'info_retention' : False,
                                  'inplace_option' : False,
                                  'defaultparams' : {'convention' : 'commas',
                                                     'test_same_as_train' : False},
                                  'NArowtype' : 'parsenumeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'nmc7'}})
    process_dict.update({'nmc8' : {'dualprocess' : self._process_nmr4,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_nmr4,
                                  'inverseprocess' : self._inverseprocess_nmrc,
                                  'info_retention' : False,
                                  'inplace_option' : False,
                                  'defaultparams' : {'convention' : 'commas',
                                                     'test_same_as_train' : False},
                                  'NArowtype' : 'parsenumeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'nmbr'}})
    process_dict.update({'nmc9' : {'dualprocess' : self._process_nmr4,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_nmr4,
                                  'inverseprocess' : self._inverseprocess_nmrc,
                                  'info_retention' : False,
                                  'inplace_option' : False,
                                  'defaultparams' : {'convention' : 'commas',
                                                     'test_same_as_train' : False},
                                  'NArowtype' : 'parsenumeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'mnmx'}})
    process_dict.update({'nmEU' : {'dualprocess' : None,
                                  'singleprocess' : self._process_nmrc,
                                  'postprocess' : None,
                                  'inverseprocess' : self._inverseprocess_nmrc,
                                  'info_retention' : True,
                                  'inplace_option' : False,
                                  'defaultparams' : {'convention' : 'spaces'},
                                  'NArowtype' : 'parsenumeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'nmEU'}})
    process_dict.update({'nmE2' : {'dualprocess' : None,
                                  'singleprocess' : self._process_nmrc,
                                  'postprocess' : None,
                                  'inverseprocess' : self._inverseprocess_nmrc,
                                  'info_retention' : False,
                                  'inplace_option' : False,
                                  'defaultparams' : {'convention' : 'spaces'},
                                  'NArowtype' : 'parsenumeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'nmbr'}})
    process_dict.update({'nmE3' : {'dualprocess' : None,
                                  'singleprocess' : self._process_nmrc,
                                  'postprocess' : None,
                                  'inverseprocess' : self._inverseprocess_nmrc,
                                  'info_retention' : False,
                                  'inplace_option' : False,
                                  'defaultparams' : {'convention' : 'spaces'},
                                  'NArowtype' : 'parsenumeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'mnmx'}})
    process_dict.update({'nmE4' : {'dualprocess' : self._process_nmr4,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_nmr4,
                                  'inverseprocess' : self._inverseprocess_nmrc,
                                  'info_retention' : True,
                                  'inplace_option' : False,
                                  'defaultparams' : {'convention' : 'spaces',
                                                     'test_same_as_train' : True},
                                  'NArowtype' : 'parsenumeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'nmE4'}})
    process_dict.update({'nmE5' : {'dualprocess' : self._process_nmr4,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_nmr4,
                                  'inverseprocess' : self._inverseprocess_nmrc,
                                  'info_retention' : False,
                                  'inplace_option' : False,
                                  'defaultparams' : {'convention' : 'spaces',
                                                     'test_same_as_train' : True},
                                  'NArowtype' : 'parsenumeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'nmbr'}})
    process_dict.update({'nmE6' : {'dualprocess' : self._process_nmr4,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_nmr4,
                                  'inverseprocess' : self._inverseprocess_nmrc,
                                  'info_retention' : False,
                                  'inplace_option' : False,
                                  'defaultparams' : {'convention' : 'spaces',
                                                     'test_same_as_train' : True},
                                  'NArowtype' : 'parsenumeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'mnmx'}})
    process_dict.update({'nmE7' : {'dualprocess' : self._process_nmr4,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_nmr4,
                                  'inverseprocess' : self._inverseprocess_nmrc,
                                  'info_retention' : False,
                                  'inplace_option' : False,
                                  'defaultparams' : {'convention' : 'spaces',
                                                     'test_same_as_train' : False},
                                  'NArowtype' : 'parsenumeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'nmE7'}})
    process_dict.update({'nmE8' : {'dualprocess' : self._process_nmr4,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_nmr4,
                                  'inverseprocess' : self._inverseprocess_nmrc,
                                  'info_retention' : False,
                                  'inplace_option' : False,
                                  'defaultparams' : {'convention' : 'spaces',
                                                     'test_same_as_train' : False},
                                  'NArowtype' : 'parsenumeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'nmbr'}})
    process_dict.update({'nmE9' : {'dualprocess' : self._process_nmr4,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_nmr4,
                                  'inverseprocess' : self._inverseprocess_nmrc,
                                  'info_retention' : False,
                                  'inplace_option' : False,
                                  'defaultparams' : {'convention' : 'spaces',
                                                     'test_same_as_train' : False},
                                  'NArowtype' : 'parsenumeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'mnmx'}})
    process_dict.update({'ors7' : {'dualprocess' : self._process_spl2,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_spl2,
                                  'inverseprocess' : self._inverseprocess_spl2,
                                  'info_retention' : False,
                                  'inplace_option' : False,
                                  'defaultparams' : {'test_same_as_train' : False,
                                                     'consolidate_nonoverlaps' : True},
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'exclude',
                                  'labelctgy' : 'ord3'}})
    process_dict.update({'ors5' : {'dualprocess' : self._process_spl2,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_spl2,
                                  'inverseprocess' : self._inverseprocess_spl2,
                                  'info_retention' : False,
                                  'inplace_option' : False,
                                  'defaultparams' : {'test_same_as_train' : False,
                                                     'consolidate_nonoverlaps' : True},
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'exclude',
                                  'labelctgy' : 'ord3'}})
    process_dict.update({'ors6' : {'dualprocess' : self._process_spl2,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_spl2,
                                  'inverseprocess' : self._inverseprocess_spl2,
                                  'info_retention' : False,
                                  'inplace_option' : False,
                                  'defaultparams' : {'test_same_as_train' : False,
                                                     'consolidate_nonoverlaps' : True},
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'exclude',
                                  'labelctgy' : 'ord3'}})
    process_dict.update({'ordl' : {'dualprocess' : self._process_ordl,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_ordl,
                                  'inverseprocess' : self._inverseprocess_ordl,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'singlct',
                                  'labelctgy' : 'ordl'}})
    process_dict.update({'ord2' : {'dualprocess' : self._process_ordl,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_ordl,
                                  'inverseprocess' : self._inverseprocess_ordl,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'singlct',
                                  'labelctgy' : 'mnmx'}})
    process_dict.update({'ord3' : {'dualprocess' : self._process_ord3,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_ord3,
                                  'inverseprocess' : self._inverseprocess_ord3,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'singlct',
                                  'labelctgy' : 'ord3'}})
    process_dict.update({'ord5' : {'dualprocess' : self._process_ordl,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_ordl,
                                  'inverseprocess' : self._inverseprocess_ordl,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'exclude',
                                  'labelctgy' : 'ord5'}})
    process_dict.update({'maxb' : {'dualprocess' : self._process_maxb,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_maxb,
                                  'inverseprocess' : self._inverseprocess_UPCS,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'singlct',
                                  'labelctgy' : 'maxb'}})
    process_dict.update({'or3b' : {'dualprocess' : self._process_ord3,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_ord3,
                                  'inverseprocess' : self._inverseprocess_ord3,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'singlct',
                                  'labelctgy' : 'maxb'}})
    process_dict.update({'matx' : {'dualprocess' : self._process_maxb,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_maxb,
                                  'inverseprocess' : self._inverseprocess_UPCS,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'singlct',
                                  'labelctgy' : 'onht'}})
    process_dict.update({'or3c' : {'dualprocess' : self._process_ord3,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_ord3,
                                  'inverseprocess' : self._inverseprocess_ord3,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'singlct',
                                  'labelctgy' : 'onht'}})
    process_dict.update({'ma10' : {'dualprocess' : self._process_maxb,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_maxb,
                                  'inverseprocess' : self._inverseprocess_UPCS,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'singlct',
                                  'labelctgy' : '1010'}})
    process_dict.update({'or3d' : {'dualprocess' : self._process_ord3,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_ord3,
                                  'inverseprocess' : self._inverseprocess_ord3,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'singlct',
                                  'labelctgy' : '1010'}})
    process_dict.update({'ucct' : {'dualprocess' : self._process_ucct,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_ucct,
                                  'inplace_option' : False,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'ucct'}})
    process_dict.update({'ord4' : {'dualprocess' : self._process_ord3,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_ord3,
                                  'inverseprocess' : self._inverseprocess_ord3,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'singlct',
                                  'labelctgy' : 'mnmx'}})
    process_dict.update({'ors2' : {'dualprocess' : self._process_spl2,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_spl2,
                                  'inverseprocess' : self._inverseprocess_spl2,
                                  'info_retention' : False,
                                  'inplace_option' : False,
                                  'defaultparams' : {'test_same_as_train' : False,
                                                     'consolidate_nonoverlaps' : False},
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'exclude',
                                  'labelctgy' : 'ord3'}})
    process_dict.update({'or10' : {'dualprocess' : None,
                                  'singleprocess' : None,
                                  'postprocess' : None,
                                  'inplace_option' : False,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'exclude',
                                  'labelctgy' : 'mnmx'}})
    process_dict.update({'or11' : {'dualprocess' : self._process_1010,
                                   'singleprocess' : None,
                                   'postprocess' : self._postprocess_1010,
                                   'inverseprocess' : self._inverseprocess_1010,
                                   'info_retention' : True,
                                   'inplace_option' : False,
                                   'NArowtype' : 'justNaN',
                                   'MLinfilltype' : '1010',
                                   'labelctgy' : 'ord3'}})
    process_dict.update({'or12' : {'dualprocess' : self._process_1010,
                                   'singleprocess' : None,
                                   'postprocess' : self._postprocess_1010,
                                   'inverseprocess' : self._inverseprocess_1010,
                                   'info_retention' : True,
                                   'inplace_option' : False,
                                   'NArowtype' : 'justNaN',
                                   'MLinfilltype' : '1010',
                                   'labelctgy' : 'ord3'}})
    process_dict.update({'or13' : {'dualprocess' : self._process_1010,
                                   'singleprocess' : None,
                                   'postprocess' : self._postprocess_1010,
                                   'inverseprocess' : self._inverseprocess_1010,
                                   'info_retention' : True,
                                   'inplace_option' : False,
                                   'NArowtype' : 'justNaN',
                                   'MLinfilltype' : '1010',
                                   'labelctgy' : 'ord3'}})
    process_dict.update({'or14' : {'dualprocess' : self._process_1010,
                                   'singleprocess' : None,
                                   'postprocess' : self._postprocess_1010,
                                   'inverseprocess' : self._inverseprocess_1010,
                                   'info_retention' : True,
                                   'inplace_option' : False,
                                   'NArowtype' : 'justNaN',
                                   'MLinfilltype' : '1010',
                                   'labelctgy' : 'ord3'}})
    process_dict.update({'or15' : {'dualprocess' : None,
                                   'singleprocess' : self._process_UPCS,
                                   'postprocess' : None,
                                   'inverseprocess' : self._inverseprocess_UPCS,
                                   'info_retention' : False,
                                   'inplace_option' : True,
                                   'NArowtype' : 'justNaN',
                                   'MLinfilltype' : 'exclude',
                                   'labelctgy' : 'ord3'}})
    process_dict.update({'or16' : {'dualprocess' : None,
                                   'singleprocess' : self._process_UPCS,
                                   'postprocess' : None,
                                   'inverseprocess' : self._inverseprocess_UPCS,
                                   'info_retention' : False,
                                   'inplace_option' : True,
                                   'NArowtype' : 'justNaN',
                                   'MLinfilltype' : 'exclude',
                                   'labelctgy' : 'ord3'}})
    process_dict.update({'or17' : {'dualprocess' : None,
                                   'singleprocess' : self._process_UPCS,
                                   'postprocess' : None,
                                   'inverseprocess' : self._inverseprocess_UPCS,
                                   'info_retention' : False,
                                   'inplace_option' : True,
                                   'NArowtype' : 'justNaN',
                                   'MLinfilltype' : 'exclude',
                                   'labelctgy' : 'ord3'}})
    process_dict.update({'or18' : {'dualprocess' : None,
                                   'singleprocess' : self._process_UPCS,
                                   'postprocess' : None,
                                   'inverseprocess' : self._inverseprocess_UPCS,
                                   'info_retention' : False,
                                   'inplace_option' : True,
                                   'NArowtype' : 'justNaN',
                                   'MLinfilltype' : 'exclude',
                                   'labelctgy' : 'ord3'}})
    process_dict.update({'or19' : {'dualprocess' : None,
                                   'singleprocess' : self._process_UPCS,
                                   'postprocess' : None,
                                   'inverseprocess' : self._inverseprocess_UPCS,
                                   'info_retention' : False,
                                   'inplace_option' : True,
                                   'NArowtype' : 'justNaN',
                                   'MLinfilltype' : 'exclude',
                                   'labelctgy' : 'ord3'}})
    process_dict.update({'or20' : {'dualprocess' : None,
                                   'singleprocess' : self._process_UPCS,
                                   'postprocess' : None,
                                   'inverseprocess' : self._inverseprocess_UPCS,
                                   'info_retention' : False,
                                   'inplace_option' : True,
                                   'NArowtype' : 'justNaN',
                                   'MLinfilltype' : 'exclude',
                                   'labelctgy' : 'ord3'}})
    process_dict.update({'or21' : {'dualprocess' : None,
                                   'singleprocess' : self._process_UPCS,
                                   'postprocess' : None,
                                   'inverseprocess' : self._inverseprocess_UPCS,
                                   'info_retention' : False,
                                   'inplace_option' : True,
                                   'NArowtype' : 'justNaN',
                                   'MLinfilltype' : 'exclude',
                                   'labelctgy' : 'ord3'}})
    process_dict.update({'or22' : {'dualprocess' : None,
                                   'singleprocess' : self._process_UPCS,
                                   'postprocess' : None,
                                   'inverseprocess' : self._inverseprocess_UPCS,
                                   'info_retention' : False,
                                   'inplace_option' : True,
                                   'NArowtype' : 'justNaN',
                                   'MLinfilltype' : 'exclude',
                                   'labelctgy' : 'ord3'}})
    process_dict.update({'or23' : {'dualprocess' : None,
                                   'singleprocess' : self._process_UPCS,
                                   'postprocess' : None,
                                   'inverseprocess' : self._inverseprocess_UPCS,
                                   'info_retention' : False,
                                   'inplace_option' : True,
                                   'NArowtype' : 'justNaN',
                                   'MLinfilltype' : 'exclude',
                                   'labelctgy' : 'ord3'}})
    process_dict.update({'om10' : {'dualprocess' : None,
                                  'singleprocess' : None,
                                  'postprocess' : None,
                                  'inplace_option' : False,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'exclude',
                                  'labelctgy' : 'mnmx'}})
    process_dict.update({'mmor' : {'dualprocess' : None,
                                  'singleprocess' : None,
                                  'postprocess' : None,
                                  'inplace_option' : False,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'mnmx'}})
    process_dict.update({'1010' : {'dualprocess' : self._process_1010,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_1010,
                                  'inverseprocess' : self._inverseprocess_1010,
                                  'info_retention' : True,
                                  'inplace_option' : False,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : '1010',
                                  'labelctgy' : '1010'}})
    process_dict.update({'qttf' : {'dualprocess' : self._process_qttf,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_qttf,
                                  'inverseprocess' : self._inverseprocess_qttf,
                                  'info_retention' : True,
                                  'inplace_option' : False,
                                  'defaultparams' : {'output_distribution' : 'normal'},
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'qttf'}})
    process_dict.update({'qtt2' : {'dualprocess' : self._process_qttf,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_qttf,
                                  'inverseprocess' : self._inverseprocess_qttf,
                                  'info_retention' : True,
                                  'inplace_option' : False,
                                  'defaultparams' : {'output_distribution' : 'uniform'},
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'qtt2'}})
    process_dict.update({'bxcx' : {'dualprocess' : self._process_bxcx,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_bxcx,
                                  'inplace_option' : False,
                                  'NArowtype' : 'positivenumeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'nmbr'}})
    process_dict.update({'tmsc' : {'dualprocess' : None,
                                  'singleprocess' : None,
                                  'postprocess' : None,
                                  'inplace_option' : False,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'tmsc'}})
    process_dict.update({'time' : {'dualprocess' : None,
                                  'singleprocess' : None,
                                  'postprocess' : None,
                                  'inplace_option' : False,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'time'}})
    process_dict.update({'tmzn' : {'dualprocess' : None,
                                  'singleprocess' : self._process_tmzn,
                                  'postprocess' : None,
                                  'inplace_option' : True,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'exclude',
                                  'labelctgy' : 'tmzn'}})
    process_dict.update({'date' : {'dualprocess' : None,
                                  'singleprocess' : self._process_tmzn,
                                  'postprocess' : None,
                                  'inplace_option' : True,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'exclude',
                                  'labelctgy' : 'time'}})
    process_dict.update({'dat2' : {'dualprocess' : None,
                                  'singleprocess' : self._process_tmzn,
                                  'postprocess' : None,
                                  'inplace_option' : True,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'exclude',
                                  'labelctgy' : 'hldy'}})
    process_dict.update({'dat3' : {'dualprocess' : None,
                                  'singleprocess' : self._process_tmzn,
                                  'postprocess' : None,
                                  'inplace_option' : True,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'exclude',
                                  'labelctgy' : 'year'}})
    process_dict.update({'dat4' : {'dualprocess' : None,
                                  'singleprocess' : self._process_tmzn,
                                  'postprocess' : None,
                                  'inplace_option' : True,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'exclude',
                                  'labelctgy' : 'year'}})
    process_dict.update({'dat5' : {'dualprocess' : None,
                                  'singleprocess' : self._process_tmzn,
                                  'postprocess' : None,
                                  'inplace_option' : True,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'exclude',
                                  'labelctgy' : 'year'}})
    process_dict.update({'dat6' : {'dualprocess' : None,
                                  'singleprocess' : self._process_tmzn,
                                  'postprocess' : None,
                                  'inplace_option' : True,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'exclude',
                                  'labelctgy' : 'year'}})
    process_dict.update({'year' : {'dualprocess' : self._process_time,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_time,
                                  'inverseprocess' : self._inverseprocess_year,
                                  'info_retention' : False,
                                  'defaultparams' : {'scale' : 'year',
                                                     'normalization' : 'zscore'},
                                  'inplace_option' : True,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'year'}})
    process_dict.update({'yea2' : {'dualprocess' : None,
                                  'singleprocess' : None,
                                  'postprocess' : None,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'year'}})
    process_dict.update({'yrsn' : {'dualprocess' : self._process_tmsc,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_tmsc,
                                  'defaultparams' : {'scale' : 'year',
                                                     'function' : 'sin'},
                                  'inplace_option' : True,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'yrsn'}})
    process_dict.update({'yrcs' : {'dualprocess' : self._process_tmsc,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_tmsc,
                                  'defaultparams' : {'scale' : 'year',
                                                     'function' : 'cos'},
                                  'inplace_option' : True,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'yrcs'}})
    process_dict.update({'mnth' : {'dualprocess' : self._process_time,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_time,
                                  'defaultparams' : {'scale' : 'month',
                                                     'normalization' : 'zscore'},
                                  'inplace_option' : True,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'mnth'}})
    process_dict.update({'mnt2' : {'dualprocess' : None,
                                  'singleprocess' : None,
                                  'postprocess' : None,
                                  'inplace_option' : False,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'mnsn'}})
    process_dict.update({'mnt3' : {'dualprocess' : None,
                                  'singleprocess' : None,
                                  'postprocess' : None,
                                  'inplace_option' : False,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'mnsn'}})
    process_dict.update({'mnt4' : {'dualprocess' : None,
                                  'singleprocess' : None,
                                  'postprocess' : None,
                                  'inplace_option' : False,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'mdsn'}})
    process_dict.update({'mnt5' : {'dualprocess' : None,
                                  'singleprocess' : None,
                                  'postprocess' : None,
                                  'inplace_option' : False,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'mdsn'}})
    process_dict.update({'mnt6' : {'dualprocess' : None,
                                  'singleprocess' : None,
                                  'postprocess' : None,
                                  'inplace_option' : False,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'mdsn'}})
    process_dict.update({'mnsn' : {'dualprocess' : self._process_tmsc,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_tmsc,
                                  'defaultparams' : {'scale' : 'month',
                                                     'function' : 'sin'},
                                  'inplace_option' : True,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'mnsn'}})
    process_dict.update({'mncs' : {'dualprocess' : self._process_tmsc,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_tmsc,
                                  'defaultparams' : {'scale' : 'month',
                                                     'function' : 'cos'},
                                  'inplace_option' : True,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'mncs'}})
    process_dict.update({'mdsn' : {'dualprocess' : self._process_tmsc,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_tmsc,
                                  'defaultparams' : {'scale' : 'monthday',
                                                     'function' : 'sin'},
                                  'inplace_option' : True,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'mdsn'}})
    process_dict.update({'mdcs' : {'dualprocess' : self._process_tmsc,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_tmsc,
                                  'defaultparams' : {'scale' : 'monthday',
                                                     'function' : 'cos'},
                                  'inplace_option' : True,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'mdcs'}})
    process_dict.update({'days' : {'dualprocess' : self._process_time,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_time,
                                  'defaultparams' : {'scale' : 'day',
                                                     'normalization' : 'zscore'},
                                  'inplace_option' : True,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'days'}})
    process_dict.update({'day2' : {'dualprocess' : None,
                                  'singleprocess' : None,
                                  'postprocess' : None,
                                  'inplace_option' : False,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'dysn'}})
    process_dict.update({'day3' : {'dualprocess' : None,
                                  'singleprocess' : None,
                                  'postprocess' : None,
                                  'inplace_option' : False,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'dysn'}})
    process_dict.update({'day4' : {'dualprocess' : None,
                                  'singleprocess' : None,
                                  'postprocess' : None,
                                  'inplace_option' : False,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'dhms'}})
    process_dict.update({'day5' : {'dualprocess' : None,
                                  'singleprocess' : None,
                                  'postprocess' : None,
                                  'inplace_option' : False,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'dhms'}})
    process_dict.update({'dysn' : {'dualprocess' : self._process_tmsc,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_tmsc,
                                  'defaultparams' : {'scale' : 'day',
                                                     'function' : 'sin'},
                                  'inplace_option' : True,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'dysn'}})
    process_dict.update({'dycs' : {'dualprocess' : self._process_tmsc,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_tmsc,
                                  'defaultparams' : {'scale' : 'day',
                                                     'function' : 'cos'},
                                  'inplace_option' : True,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'dycs'}})
    process_dict.update({'dhms' : {'dualprocess' : self._process_tmsc,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_tmsc,
                                  'defaultparams' : {'scale' : 'dayhourminute',
                                                     'function' : 'sin'},
                                  'inplace_option' : True,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'dhms'}})
    process_dict.update({'dhmc' : {'dualprocess' : self._process_tmsc,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_tmsc,
                                  'defaultparams' : {'scale' : 'dayhourminute',
                                                     'function' : 'cos'},
                                  'inplace_option' : True,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'dhmc'}})
    process_dict.update({'hour' : {'dualprocess' : self._process_time,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_time,
                                  'defaultparams' : {'scale' : 'hour',
                                                     'normalization' : 'zscore'},
                                  'inplace_option' : True,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'hour'}})
    process_dict.update({'hrs2' : {'dualprocess' : None,
                                  'singleprocess' : None,
                                  'postprocess' : None,
                                  'inplace_option' : False,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'hrsn'}})
    process_dict.update({'hrs3' : {'dualprocess' : None,
                                  'singleprocess' : None,
                                  'postprocess' : None,
                                  'inplace_option' : False,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'hrsn'}})
    process_dict.update({'hrs4' : {'dualprocess' : None,
                                  'singleprocess' : None,
                                  'postprocess' : None,
                                  'inplace_option' : False,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'hmss'}})
    process_dict.update({'hrsn' : {'dualprocess' : self._process_tmsc,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_tmsc,
                                  'defaultparams' : {'scale' : 'hour',
                                                     'function' : 'sin'},
                                  'inplace_option' : True,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'hrsn'}})
    process_dict.update({'hrcs' : {'dualprocess' : self._process_tmsc,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_tmsc,
                                  'defaultparams' : {'scale' : 'hour',
                                                     'function' : 'cos'},
                                  'inplace_option' : True,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'hrcs'}})
    process_dict.update({'hmss' : {'dualprocess' : self._process_tmsc,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_tmsc,
                                  'defaultparams' : {'scale' : 'hourminutesecond',
                                                     'function' : 'sin'},
                                  'inplace_option' : True,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'hmss'}})
    process_dict.update({'hmsc' : {'dualprocess' : self._process_tmsc,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_tmsc,
                                  'defaultparams' : {'scale' : 'hourminutesecond',
                                                     'function' : 'cos'},
                                  'inplace_option' : True,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'hmsc'}})
    process_dict.update({'mint' : {'dualprocess' : self._process_time,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_time,
                                  'defaultparams' : {'scale' : 'minute',
                                                     'normalization' : 'zscore'},
                                  'inplace_option' : True,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'mint'}})
    process_dict.update({'min2' : {'dualprocess' : None,
                                  'singleprocess' : None,
                                  'postprocess' : None,
                                  'inplace_option' : False,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'misn'}})
    process_dict.update({'min3' : {'dualprocess' : None,
                                  'singleprocess' : None,
                                  'postprocess' : None,
                                  'inplace_option' : False,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'misn'}})
    process_dict.update({'min4' : {'dualprocess' : None,
                                  'singleprocess' : None,
                                  'postprocess' : None,
                                  'inplace_option' : False,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'mssn'}})
    process_dict.update({'misn' : {'dualprocess' : self._process_tmsc,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_tmsc,
                                  'defaultparams' : {'scale' : 'minute',
                                                     'function' : 'sin'},
                                  'inplace_option' : True,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'misn'}})
    process_dict.update({'mics' : {'dualprocess' : self._process_tmsc,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_tmsc,
                                  'defaultparams' : {'scale' : 'minute',
                                                     'function' : 'cos'},
                                  'inplace_option' : True,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'mics'}})
    process_dict.update({'mssn' : {'dualprocess' : self._process_tmsc,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_tmsc,
                                  'defaultparams' : {'scale' : 'minutesecond',
                                                     'function' : 'sin'},
                                  'inplace_option' : True,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'mssn'}})
    process_dict.update({'mscs' : {'dualprocess' : self._process_tmsc,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_tmsc,
                                  'defaultparams' : {'scale' : 'minutesecond',
                                                     'function' : 'cos'},
                                  'inplace_option' : True,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'mscs'}})
    process_dict.update({'scnd' : {'dualprocess' : self._process_time,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_time,
                                  'defaultparams' : {'scale' : 'second',
                                                     'normalization' : 'zscore'},
                                  'inplace_option' : True,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'scnd'}})
    process_dict.update({'scn2' : {'dualprocess' : None,
                                  'singleprocess' : None,
                                  'postprocess' : None,
                                  'inplace_option' : False,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'scsn'}})
    process_dict.update({'scsn' : {'dualprocess' : self._process_tmsc,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_tmsc,
                                  'defaultparams' : {'scale' : 'second',
                                                     'function' : 'sin'},
                                  'inplace_option' : True,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'scsn'}})
    process_dict.update({'sccs' : {'dualprocess' : self._process_tmsc,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_tmsc,
                                  'defaultparams' : {'scale' : 'second',
                                                     'function' : 'cos'},
                                  'inplace_option' : True,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'sccs'}})
    process_dict.update({'bxc2' : {'dualprocess' : self._process_bxcx,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_bxcx,
                                  'inplace_option' : False,
                                  'NArowtype' : 'nonzeronumeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'nmbr'}})
    process_dict.update({'bxc3' : {'dualprocess' : self._process_bxcx,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_bxcx,
                                  'inplace_option' : False,
                                  'NArowtype' : 'positivenumeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'nmbr'}})
    process_dict.update({'bxc4' : {'dualprocess' : self._process_bxcx,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_bxcx,
                                  'inplace_option' : False,
                                  'NArowtype' : 'positivenumeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'nbr2'}})
    process_dict.update({'bxc5' : {'dualprocess' : self._process_bxcx,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_bxcx,
                                  'inplace_option' : False,
                                  'NArowtype' : 'positivenumeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'nbr2'}})
    process_dict.update({'ntgr' : {'dualprocess' : self._process_ord3,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_ord3,
                                  'inverseprocess' : self._inverseprocess_ord3,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'integer',
                                  'MLinfilltype' : 'singlct',
                                  'labelctgy' : 'mnmx'}})
    process_dict.update({'ntg2' : {'dualprocess' : self._process_ord3,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_ord3,
                                  'inverseprocess' : self._inverseprocess_ord3,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'integer',
                                  'MLinfilltype' : 'singlct',
                                  'labelctgy' : 'mnmx'}})
    process_dict.update({'ntg3' : {'dualprocess' : self._process_ord3,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_ord3,
                                  'inverseprocess' : self._inverseprocess_ord3,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'integer',
                                  'MLinfilltype' : 'singlct',
                                  'labelctgy' : 'mnmx'}})
    process_dict.update({'pwrs' : {'dualprocess' : self._process_pwrs,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_pwrs,
                                  'inverseprocess' : self._inverseprocess_pwr2,
                                  'info_retention' : False,
                                  'inplace_option' : False,
                                  'NArowtype' : 'positivenumeric',
                                  'MLinfilltype' : 'multirt',
                                  'labelctgy' : 'pwrs'}})
    process_dict.update({'pwr2' : {'dualprocess' : self._process_pwrs,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_pwrs,
                                  'inverseprocess' : self._inverseprocess_pwr2,
                                  'info_retention' : False,
                                  'inplace_option' : False,
                                  'defaultparams' : {'negvalues' : True},
                                  'NArowtype' : 'nonzeronumeric',
                                  'MLinfilltype' : 'multirt',
                                  'labelctgy' : 'pwr2'}})
    process_dict.update({'log0' : {'dualprocess' : self._process_log0,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_log0,
                                  'inverseprocess' : self._inverseprocess_log0,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'positivenumeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'log0'}})
    process_dict.update({'log1' : {'dualprocess' : self._process_log0,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_log0,
                                  'inverseprocess' : self._inverseprocess_log0,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'positivenumeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'log0'}})
    process_dict.update({'logn' : {'dualprocess' : self._process_logn,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_logn,
                                  'inverseprocess' : self._inverseprocess_logn,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'positivenumeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'logn'}})
    process_dict.update({'lgnm' : {'dualprocess' : self._process_logn,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_logn,
                                  'inverseprocess' : self._inverseprocess_logn,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'positivenumeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'nmbr'}})
    process_dict.update({'sqrt' : {'dualprocess' : self._process_sqrt,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_sqrt,
                                  'inverseprocess' : self._inverseprocess_sqrt,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'nonnegativenumeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'sqrt'}})
    process_dict.update({'addd' : {'dualprocess' : self._process_addd,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_addd,
                                  'inverseprocess' : self._inverseprocess_addd,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'addd'}})
    process_dict.update({'sbtr' : {'dualprocess' : self._process_sbtr,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_sbtr,
                                  'inverseprocess' : self._inverseprocess_sbtr,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'sbtr'}})
    process_dict.update({'mltp' : {'dualprocess' : self._process_mltp,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_mltp,
                                  'inverseprocess' : self._inverseprocess_mltp,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'mltp'}})
    process_dict.update({'divd' : {'dualprocess' : self._process_divd,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_divd,
                                  'inverseprocess' : self._inverseprocess_divd,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'divd'}})
    process_dict.update({'rais' : {'dualprocess' : self._process_rais,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_rais,
                                  'inverseprocess' : self._inverseprocess_rais,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'rais'}})
    process_dict.update({'absl' : {'dualprocess' : self._process_absl,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_absl,
                                  'inverseprocess' : self._inverseprocess_absl,
                                  'info_retention' : False,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'absl'}})
    process_dict.update({'bkt1' : {'dualprocess' : self._process_bkt1,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_bkt1,
                                  'inverseprocess' : self._inverseprocess_bkt1,
                                  'info_retention' : False,
                                  'inplace_option' : False,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'multirt',
                                  'labelctgy' : 'bkt1'}})
    process_dict.update({'bkt2' : {'dualprocess' : self._process_bkt2,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_bkt2,
                                  'inverseprocess' : self._inverseprocess_bkt2,
                                  'info_retention' : False,
                                  'inplace_option' : False,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'multirt',
                                  'labelctgy' : 'bkt2'}})
    process_dict.update({'bkt3' : {'dualprocess' : self._process_bkt3,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_bkt3,
                                  'inverseprocess' : self._inverseprocess_bkt3,
                                  'info_retention' : False,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'singlct',
                                  'labelctgy' : 'bkt3'}})
    process_dict.update({'bkt4' : {'dualprocess' : self._process_bkt4,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_bkt4,
                                  'inverseprocess' : self._inverseprocess_bkt4,
                                  'info_retention' : False,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'singlct',
                                  'labelctgy' : 'bkt4'}})
    process_dict.update({'wkdy' : {'dualprocess' : None,
                                  'singleprocess' : self._process_wkdy,
                                  'postprocess' : None,
                                  'inplace_option' : False,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'binary',
                                  'labelctgy' : 'wkdy'}})
    process_dict.update({'bshr' : {'dualprocess' : None,
                                  'singleprocess' : self._process_bshr,
                                  'postprocess' : None,
                                  'inplace_option' : False,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'binary',
                                  'labelctgy' : 'bshr'}})
    process_dict.update({'hldy' : {'dualprocess' : None,
                                  'singleprocess' : self._process_hldy,
                                  'postprocess' : None,
                                  'inplace_option' : False,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'binary',
                                  'labelctgy' : 'hldy'}})
    process_dict.update({'wkds' : {'dualprocess' : None,
                                  'singleprocess' : self._process_wkds,
                                  'postprocess' : None,
                                  'inplace_option' : True,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'singlct',
                                  'labelctgy' : 'text'}})
    process_dict.update({'wkdo' : {'dualprocess' : None,
                                  'singleprocess' : self._process_wkds,
                                  'postprocess' : None,
                                  'inplace_option' : True,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'singlct',
                                  'labelctgy' : 'ordl'}})
    process_dict.update({'mnts' : {'dualprocess' : None,
                                  'singleprocess' : self._process_mnts,
                                  'postprocess' : None,
                                  'inplace_option' : True,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'singlct',
                                  'labelctgy' : 'text'}})
    process_dict.update({'mnto' : {'dualprocess' : None,
                                  'singleprocess' : self._process_mnts,
                                  'postprocess' : None,
                                  'inplace_option' : True,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'singlct',
                                  'labelctgy' : 'ordl'}})
    process_dict.update({'bins' : {'dualprocess' : self._process_bins,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_bins,
                                  'inverseprocess' : self._inverseprocess_bins,
                                  'info_retention' : False,
                                  'inplace_option' : False,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'multirt',
                                  'labelctgy' : 'bins'}})
    process_dict.update({'bint' : {'dualprocess' : self._process_bins,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_bins,
                                  'inverseprocess' : self._inverseprocess_bins,
                                  'info_retention' : False,
                                  'inplace_option' : False,
                                  'defaultparams' : {'normalizedinput' : True},
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'multirt',
                                  'labelctgy' : 'bint'}})
    process_dict.update({'bsor' : {'dualprocess' : self._process_bsor,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_bsor,
                                  'inverseprocess' : self._inverseprocess_bsor,
                                  'info_retention' : False,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'singlct',
                                  'labelctgy' : 'bsor'}})
    process_dict.update({'btor' : {'dualprocess' : self._process_bsor,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_bsor,
                                  'inverseprocess' : self._inverseprocess_bsor,
                                  'info_retention' : False,
                                  'defaultparams' : {'normalizedinput' : True},
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'singlct',
                                  'labelctgy' : 'btor'}})
    process_dict.update({'bnwd' : {'dualprocess' : self._process_bnwd,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_bnwd,
                                  'inverseprocess' : self._inverseprocess_bnwd,
                                  'info_retention' : False,
                                  'inplace_option' : False,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'multirt',
                                  'labelctgy' : 'bnwd'}})
    process_dict.update({'bnwK' : {'dualprocess' : self._process_bnwd,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_bnwd,
                                  'inverseprocess' : self._inverseprocess_bnwd,
                                  'info_retention' : False,
                                  'inplace_option' : False,
                                  'defaultparams' : {'width':1000},
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'multirt',
                                  'labelctgy' : 'bnwK'}})
    process_dict.update({'bnwM' : {'dualprocess' : self._process_bnwd,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_bnwd,
                                  'inverseprocess' : self._inverseprocess_bnwd,
                                  'info_retention' : False,
                                  'inplace_option' : False,
                                  'defaultparams' : {'width':1000000},
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'multirt',
                                  'labelctgy' : 'bnwM'}})
    process_dict.update({'bnwo' : {'dualprocess' : self._process_bnwo,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_bnwo,
                                  'inverseprocess' : self._inverseprocess_bnwo,
                                  'info_retention' : False,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'singlct',
                                  'labelctgy' : 'bnwo'}})
    process_dict.update({'bnKo' : {'dualprocess' : self._process_bnwo,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_bnwo,
                                  'inverseprocess' : self._inverseprocess_bnwo,
                                  'info_retention' : False,
                                  'inplace_option' : True,
                                  'defaultparams' : {'width':1000},
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'singlct',
                                  'labelctgy' : 'bnKo'}})
    process_dict.update({'bnMo' : {'dualprocess' : self._process_bnwo,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_bnwo,
                                  'inverseprocess' : self._inverseprocess_bnwo,
                                  'info_retention' : False,
                                  'inplace_option' : True,
                                  'defaultparams' : {'width':1000000},
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'singlct',
                                  'labelctgy' : 'bnMo'}})
    process_dict.update({'bnep' : {'dualprocess' : self._process_bnep,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_bnep,
                                  'inverseprocess' : self._inverseprocess_bnep,
                                  'info_retention' : False,
                                  'inplace_option' : False,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'multirt',
                                  'labelctgy' : 'bnep'}})
    process_dict.update({'bne7' : {'dualprocess' : self._process_bnep,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_bnep,
                                  'inverseprocess' : self._inverseprocess_bnep,
                                  'info_retention' : False,
                                  'inplace_option' : False,
                                  'defaultparams' : {'bincount':7},
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'multirt',
                                  'labelctgy' : 'bne7'}})
    process_dict.update({'bne9' : {'dualprocess' : self._process_bnep,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_bnep,
                                  'inverseprocess' : self._inverseprocess_bnep,
                                  'info_retention' : False,
                                  'inplace_option' : False,
                                  'defaultparams' : {'bincount':9},
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'multirt',
                                  'labelctgy' : 'bne9'}})
    process_dict.update({'bneo' : {'dualprocess' : self._process_bneo,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_bneo,
                                  'inverseprocess' : self._inverseprocess_bneo,
                                  'info_retention' : False,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'singlct',
                                  'labelctgy' : 'bneo'}})
    process_dict.update({'bn7o' : {'dualprocess' : self._process_bneo,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_bneo,
                                  'inverseprocess' : self._inverseprocess_bneo,
                                  'info_retention' : False,
                                  'defaultparams' : {'bincount':7},
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'singlct',
                                  'labelctgy' : 'bn7o'}})
    process_dict.update({'bn9o' : {'dualprocess' : self._process_bneo,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_bneo,
                                  'inverseprocess' : self._inverseprocess_bneo,
                                  'info_retention' : False,
                                  'defaultparams' : {'bincount':9},
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'singlct',
                                  'labelctgy' : 'bn9o'}})
    process_dict.update({'tlbn' : {'dualprocess' : self._process_tlbn,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_tlbn,
                                  'inverseprocess' : self._inverseprocess_tlbn,
                                  'info_retention' : True,
                                  'inplace_option' : False,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'concurrent_nmbr',
                                  'labelctgy' : 'tlbn'}})
    process_dict.update({'pwor' : {'dualprocess' : self._process_pwor,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_pwor,
                                  'inverseprocess' : self._inverseprocess_por2,
                                  'info_retention' : False,
                                  'inplace_option' : True,
                                  'NArowtype' : 'positivenumeric',
                                  'MLinfilltype' : 'singlct',
                                  'labelctgy' : 'pwor'}})
    process_dict.update({'por2' : {'dualprocess' : self._process_pwor,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_pwor,
                                  'inverseprocess' : self._inverseprocess_por2,
                                  'info_retention' : False,
                                  'inplace_option' : True,
                                  'defaultparams' : {'negvalues' : True},
                                  'NArowtype' : 'nonzeronumeric',
                                  'MLinfilltype' : 'singlct',
                                  'labelctgy' : 'por2'}})
    process_dict.update({'por3' : {'dualprocess' : self._process_pwor,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_pwor,
                                  'inverseprocess' : self._inverseprocess_por2,
                                  'info_retention' : False,
                                  'inplace_option' : True,
                                  'defaultparams' : {'negvalues' : True},
                                  'NArowtype' : 'nonzeronumeric',
                                  'MLinfilltype' : 'singlct',
                                  'labelctgy' : '1010'}})
    process_dict.update({'bkb3' : {'dualprocess' : self._process_bkt3,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_bkt3,
                                  'inverseprocess' : self._inverseprocess_bkt3,
                                  'info_retention' : False,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'singlct',
                                  'labelctgy' : '1010'}})
    process_dict.update({'bkb4' : {'dualprocess' : self._process_bkt4,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_bkt4,
                                  'inverseprocess' : self._inverseprocess_bkt4,
                                  'info_retention' : False,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'singlct',
                                  'labelctgy' : '1010'}})
    process_dict.update({'bsbn' : {'dualprocess' : self._process_bsor,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_bsor,
                                  'inverseprocess' : self._inverseprocess_bsor,
                                  'info_retention' : False,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'singlct',
                                  'labelctgy' : '1010'}})
    process_dict.update({'bnwb' : {'dualprocess' : self._process_bnwo,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_bnwo,
                                  'inverseprocess' : self._inverseprocess_bnwo,
                                  'info_retention' : False,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'singlct',
                                  'labelctgy' : '1010'}})
    process_dict.update({'bnKb' : {'dualprocess' : self._process_bnwo,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_bnwo,
                                  'inverseprocess' : self._inverseprocess_bnwo,
                                  'info_retention' : False,
                                  'defaultparams' : {'width':1000},
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'singlct',
                                  'labelctgy' : '1010'}})
    process_dict.update({'bnMb' : {'dualprocess' : self._process_bnwo,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_bnwo,
                                  'inverseprocess' : self._inverseprocess_bnwo,
                                  'info_retention' : False,
                                  'defaultparams' : {'width':1000000},
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'singlct',
                                  'labelctgy' : '1010'}})
    process_dict.update({'bneb' : {'dualprocess' : self._process_bneo,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_bneo,
                                  'inverseprocess' : self._inverseprocess_bneo,
                                  'info_retention' : False,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'singlct',
                                  'labelctgy' : '1010'}})
    process_dict.update({'bn7b' : {'dualprocess' : self._process_bneo,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_bneo,
                                  'inverseprocess' : self._inverseprocess_bneo,
                                  'info_retention' : False,
                                  'defaultparams' : {'bincount':7},
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'singlct',
                                  'labelctgy' : '1010'}})
    process_dict.update({'bn9b' : {'dualprocess' : self._process_bneo,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_bneo,
                                  'inverseprocess' : self._inverseprocess_bneo,
                                  'info_retention' : False,
                                  'defaultparams' : {'bincount':9},
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'singlct',
                                  'labelctgy' : '1010'}})
    process_dict.update({'pwbn' : {'dualprocess' : self._process_pwor,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_pwor,
                                  'inverseprocess' : self._inverseprocess_por2,
                                  'info_retention' : False,
                                  'inplace_option' : False,
                                  'NArowtype' : 'positivenumeric',
                                  'MLinfilltype' : 'singlct',
                                  'labelctgy' : '1010'}})
    process_dict.update({'DPn3' : {'dualprocess' : self._process_numerical,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_numerical,
                                  'inverseprocess' : self._inverseprocess_nmbr,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'DPnb'}})
    process_dict.update({'DPnb' : {'dualprocess' : self._process_DPnb,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_DPnb,
                                  'inverseprocess' : self._inverseprocess_UPCS,
                                  'info_retention' : True,
                                  'inplace_option' : False,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'DPnb'}})
    process_dict.update({'DPm2' : {'dualprocess' : self._process_mnmx,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_mnmx,
                                  'inverseprocess' : self._inverseprocess_mnmx,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'DPmm'}})
    process_dict.update({'DPmm' : {'dualprocess' : self._process_DPmm,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_DPmm,
                                  'inverseprocess' : self._inverseprocess_UPCS,
                                  'info_retention' : True,
                                  'inplace_option' : False,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'DPmm'}})
    process_dict.update({'DPrt' : {'dualprocess' : self._process_DPrt,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_DPrt,
                                  'inverseprocess' : self._inverseprocess_retn,
                                  'info_retention' : True,
                                  'inplace_option' : False,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'DPrt'}})
    process_dict.update({'DLn3' : {'dualprocess' : self._process_numerical,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_numerical,
                                  'inverseprocess' : self._inverseprocess_nmbr,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'DLnb'}})
    process_dict.update({'DLnb' : {'dualprocess' : self._process_DPnb,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_DPnb,
                                  'inverseprocess' : self._inverseprocess_UPCS,
                                  'info_retention' : True,
                                  'inplace_option' : False,
                                  'defaultparams' : {'noisedistribution' : 'laplace'},
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'DLnb'}})
    process_dict.update({'DLm2' : {'dualprocess' : self._process_mnmx,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_mnmx,
                                  'inverseprocess' : self._inverseprocess_mnmx,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'DLmm'}})
    process_dict.update({'DLmm' : {'dualprocess' : self._process_DPmm,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_DPmm,
                                  'inverseprocess' : self._inverseprocess_UPCS,
                                  'info_retention' : True,
                                  'inplace_option' : False,
                                  'defaultparams' : {'noisedistribution' : 'laplace'},
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'DLmm'}})
    process_dict.update({'DLrt' : {'dualprocess' : self._process_DPrt,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_DPrt,
                                  'inverseprocess' : self._inverseprocess_retn,
                                  'info_retention' : True,
                                  'inplace_option' : False,
                                  'defaultparams' : {'noisedistribution' : 'laplace'},
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'DLrt'}})
    process_dict.update({'DPb2' : {'dualprocess' : self._process_binary,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_binary,
                                  'inverseprocess' : self._inverseprocess_bnry,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'binary',
                                  'labelctgy' : 'DPbn'}})
    process_dict.update({'DPbn' : {'dualprocess' : self._process_DPbn,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_DPbn,
                                  'inverseprocess' : self._inverseprocess_UPCS,
                                  'info_retention' : True,
                                  'inplace_option' : False,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'binary',
                                  'labelctgy' : 'DPbn'}})
    process_dict.update({'DPo4' : {'dualprocess' : self._process_ord3,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_ord3,
                                  'inverseprocess' : self._inverseprocess_ord3,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'singlct',
                                  'labelctgy' : 'DPod'}})
    process_dict.update({'DPod' : {'dualprocess' : self._process_DPod,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_DPod,
                                  'inverseprocess' : self._inverseprocess_UPCS,
                                  'info_retention' : True,
                                  'inplace_option' : False,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'singlct',
                                  'labelctgy' : 'DPod'}})
    process_dict.update({'DPo5' : {'dualprocess' : self._process_ord3,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_ord3,
                                  'inverseprocess' : self._inverseprocess_ord3,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'singlct',
                                  'labelctgy' : 'onht'}})
    process_dict.update({'DPo2' : {'dualprocess' : self._process_DPod,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_DPod,
                                  'inverseprocess' : self._inverseprocess_UPCS,
                                  'info_retention' : True,
                                  'inplace_option' : False,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'singlct',
                                  'labelctgy' : 'onht'}})
    process_dict.update({'DPoh' : {'dualprocess' : self._process_DPod,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_DPod,
                                  'inverseprocess' : self._inverseprocess_UPCS,
                                  'info_retention' : True,
                                  'inplace_option' : False,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'singlct',
                                  'labelctgy' : 'onht'}})
    process_dict.update({'DP10' : {'dualprocess' : self._process_DPod,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_DPod,
                                  'inverseprocess' : self._inverseprocess_UPCS,
                                  'info_retention' : True,
                                  'inplace_option' : False,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'singlct',
                                  'labelctgy' : '1010'}})
    process_dict.update({'DPo6' : {'dualprocess' : self._process_ord3,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_ord3,
                                  'inverseprocess' : self._inverseprocess_ord3,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'singlct',
                                  'labelctgy' : '1010'}})
    process_dict.update({'DPo3' : {'dualprocess' : self._process_DPod,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_DPod,
                                  'inverseprocess' : self._inverseprocess_UPCS,
                                  'info_retention' : True,
                                  'inplace_option' : False,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'singlct',
                                  'labelctgy' : '1010'}})
    process_dict.update({'qbt1' : {'dualprocess' : None,
                                  'singleprocess' : self._process_qbt1,
                                  'postprocess' : None,
                                  'inverseprocess' : self._inverseprocess_qbt1,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'exclude',
                                  'labelctgy' : 'qbt1'}})
    process_dict.update({'qbt2' : {'dualprocess' : None,
                                  'singleprocess' : self._process_qbt1,
                                  'postprocess' : None,
                                  'inverseprocess' : self._inverseprocess_qbt1,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'defaultparams' : {'integer_bits' : 15,
                                                     'fractional_bits' : 0},
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'exclude',
                                  'labelctgy' : 'qbt2'}})
    process_dict.update({'qbt3' : {'dualprocess' : None,
                                  'singleprocess' : self._process_qbt1,
                                  'postprocess' : None,
                                  'inverseprocess' : self._inverseprocess_qbt1,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'defaultparams' : {'sign_bit' : False,
                                                     'fractional_bits' : 13},
                                  'NArowtype' : 'nonnegativenumeric',
                                  'MLinfilltype' : 'exclude',
                                  'labelctgy' : 'qbt3'}})
    process_dict.update({'qbt4' : {'dualprocess' : None,
                                  'singleprocess' : self._process_qbt1,
                                  'postprocess' : None,
                                  'inverseprocess' : self._inverseprocess_qbt1,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'defaultparams' : {'sign_bit' : False,
                                                     'integer_bits' : 16,
                                                     'fractional_bits' : 0},
                                  'NArowtype' : 'nonnegativenumeric',
                                  'MLinfilltype' : 'exclude',
                                  'labelctgy' : 'qbt4'}})
    process_dict.update({'nmqb' : {'dualprocess' : self._process_numerical,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_numerical,
                                  'inverseprocess' : self._inverseprocess_nmbr,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'qbt1'}})
    process_dict.update({'nmq2' : {'dualprocess' : self._process_numerical,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_numerical,
                                  'inverseprocess' : self._inverseprocess_nmbr,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'qbt1'}})
    process_dict.update({'mmqb' : {'dualprocess' : self._process_mnmx,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_mnmx,
                                  'inverseprocess' : self._inverseprocess_mnmx,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'qbt3'}})
    process_dict.update({'mmq2' : {'dualprocess' : self._process_mnmx,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_mnmx,
                                  'inverseprocess' : self._inverseprocess_mnmx,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'qbt3'}})
    process_dict.update({'NArw' : {'dualprocess' : None,
                                  'singleprocess' : self._process_NArw,
                                  'postprocess' : None,
                                  'inplace_option' : False,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'boolexclude',
                                  'labelctgy' : 'NArw'}})
    process_dict.update({'NAr2' : {'dualprocess' : None,
                                  'singleprocess' : self._process_NArw,
                                  'postprocess' : None,
                                  'inplace_option' : False,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'boolexclude',
                                  'labelctgy' : 'NAr2'}})
    process_dict.update({'NAr3' : {'dualprocess' : None,
                                  'singleprocess' : self._process_NArw,
                                  'postprocess' : None,
                                  'inplace_option' : False,
                                  'NArowtype' : 'positivenumeric',
                                  'MLinfilltype' : 'boolexclude',
                                  'labelctgy' : 'NAr3'}})
    process_dict.update({'NAr4' : {'dualprocess' : None,
                                  'singleprocess' : self._process_NArw,
                                  'postprocess' : None,
                                  'inplace_option' : False,
                                  'NArowtype' : 'nonnegativenumeric',
                                  'MLinfilltype' : 'boolexclude',
                                  'labelctgy' : 'NAr4'}})
    process_dict.update({'NAr5' : {'dualprocess' : None,
                                  'singleprocess' : self._process_NArw,
                                  'postprocess' : None,
                                  'inplace_option' : False,
                                  'NArowtype' : 'integer',
                                  'MLinfilltype' : 'boolexclude',
                                  'labelctgy' : 'NAr5'}})
    process_dict.update({'null' : {'dualprocess' : None,
                                  'singleprocess' : self._process_null,
                                  'postprocess' : None,
                                  'inplace_option' : False,
                                  'NArowtype' : 'exclude',
                                  'MLinfilltype' : 'exclude',
                                  'labelctgy' : None}})
    process_dict.update({'copy' : {'dualprocess' : None,
                                  'singleprocess' : self._process_copy,
                                  'postprocess' : None,
                                  'inverseprocess' : self._inverseprocess_excl,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'exclude',
                                  'MLinfilltype' : 'exclude',
                                  'labelctgy' : 'copy'}})
    process_dict.update({'excl' : {'dualprocess' : None,
                                  'singleprocess' : self._process_excl,
                                  'postprocess' : None,
                                  'inverseprocess' : self._inverseprocess_excl,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'exclude',
                                  'MLinfilltype' : 'totalexclude',
                                  'labelctgy' : 'excl'}})
    process_dict.update({'exc2' : {'dualprocess' : self._process_exc2,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_exc2,
                                  'inverseprocess' : self._inverseprocess_UPCS,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'exc2'}})
    process_dict.update({'exc3' : {'dualprocess' : self._process_exc2,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_exc2,
                                  'inverseprocess' : self._inverseprocess_UPCS,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'exc3'}})
    process_dict.update({'exc4' : {'dualprocess' : self._process_exc2,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_exc2,
                                  'inverseprocess' : self._inverseprocess_UPCS,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'exc4'}})
    process_dict.update({'exc5' : {'dualprocess' : self._process_exc5,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_exc5,
                                  'inverseprocess' : self._inverseprocess_UPCS,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'defaultparams' : {'integertype' : 'singlct'},
                                  'NArowtype' : 'integer',
                                  'MLinfilltype' : 'singlct',
                                  'labelctgy' : 'exc5'}})
    process_dict.update({'exc6' : {'dualprocess' : self._process_exc2,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_exc2,
                                  'inverseprocess' : self._inverseprocess_UPCS,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'exc6'}})
    process_dict.update({'exc7' : {'dualprocess' : self._process_exc5,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_exc5,
                                  'inverseprocess' : self._inverseprocess_UPCS,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'defaultparams' : {'integertype' : 'singlct'},
                                  'NArowtype' : 'integer',
                                  'MLinfilltype' : 'singlct',
                                  'labelctgy' : 'exc7'}})
    process_dict.update({'exc8' : {'dualprocess' : self._process_exc5,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_exc5,
                                  'inverseprocess' : self._inverseprocess_UPCS,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'defaultparams' : {'integertype' : 'integer'},
                                  'NArowtype' : 'integer',
                                  'MLinfilltype' : 'integer',
                                  'labelctgy' : 'exc8'}})
    process_dict.update({'exc9' : {'dualprocess' : self._process_exc5,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_exc5,
                                  'inverseprocess' : self._inverseprocess_UPCS,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'defaultparams' : {'integertype' : 'integer'},
                                  'NArowtype' : 'integer',
                                  'MLinfilltype' : 'integer',
                                  'labelctgy' : 'exc9'}})
    process_dict.update({'shfl' : {'dualprocess' : None,
                                  'singleprocess' : self._process_shfl,
                                  'postprocess' : None,
                                  'inplace_option' : True,
                                  'NArowtype' : 'exclude',
                                  'MLinfilltype' : 'exclude',
                                  'labelctgy' : 'shfl'}})
    process_dict.update({'nmbd' : {'dualprocess' : self._process_numerical,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_numerical,
                                  'inverseprocess' : self._inverseprocess_nmbr,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'nmbr'}})
    process_dict.update({'101d' : {'dualprocess' : self._process_1010,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_1010,
                                  'inverseprocess' : self._inverseprocess_1010,
                                  'info_retention' : True,
                                  'inplace_option' : False,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : '1010',
                                  'labelctgy' : '1010'}})
    process_dict.update({'ordd' : {'dualprocess' : self._process_ord3,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_ord3,
                                  'inverseprocess' : self._inverseprocess_ord3,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'singlct',
                                  'labelctgy' : 'ord3'}})
    process_dict.update({'texd' : {'dualprocess' : self._process_text,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_text,
                                  'inverseprocess' : self._inverseprocess_text,
                                  'info_retention' : True,
                                  'inplace_option' : False,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'multirt',
                                  'labelctgy' : 'text'}})
    process_dict.update({'bnrd' : {'dualprocess' : self._process_binary,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_binary,
                                  'inverseprocess' : self._inverseprocess_bnry,
                                  'info_retention' : True,
                                  'inplace_option' : False,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'binary',
                                  'labelctgy' : 'bnry'}})
    process_dict.update({'datd' : {'dualprocess' : None,
                                  'singleprocess' : None,
                                  'postprocess' : None,
                                  'inplace_option' : False,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'exclude',
                                  'labelctgy' : 'mdsn'}})
    process_dict.update({'nuld' : {'dualprocess' : None,
                                  'singleprocess' : self._process_null,
                                  'postprocess' : None,
                                  'inplace_option' : False,
                                  'NArowtype' : 'exclude',
                                  'MLinfilltype' : 'exclude',
                                  'labelctgy' : None}})
    process_dict.update({'lbnm' : {'dualprocess' : self._process_exc2,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_exc2,
                                  'inverseprocess' : self._inverseprocess_UPCS,
                                  'info_retention' : True,
                                  'inplace_option' : False,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'exc2'}})
    process_dict.update({'lbnb' : {'dualprocess' : self._process_numerical,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_numerical,
                                  'inverseprocess' : self._inverseprocess_nmbr,
                                  'info_retention' : True,
                                  'inplace_option' : False,
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'nmbr'}})
    process_dict.update({'lb10' : {'dualprocess' : self._process_text,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_text,
                                  'inverseprocess' : self._inverseprocess_text,
                                  'info_retention' : True,
                                  'inplace_option' : False,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'multirt',
                                  'labelctgy' : '1010'}})
    process_dict.update({'lbor' : {'dualprocess' : self._process_ordl,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_ordl,
                                  'inverseprocess' : self._inverseprocess_ordl,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'singlct',
                                  'labelctgy' : 'ordl'}})
    process_dict.update({'lbos' : {'dualprocess' : self._process_ordl,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_ordl,
                                  'inverseprocess' : self._inverseprocess_ordl,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'singlct',
                                  'labelctgy' : 'strg'}})
    process_dict.update({'lbte' : {'dualprocess' : self._process_text,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_text,
                                  'inverseprocess' : self._inverseprocess_text,
                                  'info_retention' : True,
                                  'inplace_option' : False,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'multirt',
                                  'labelctgy' : 'text'}})
    process_dict.update({'lbbn' : {'dualprocess' : self._process_binary,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_binary,
                                  'inverseprocess' : self._inverseprocess_bnry,
                                  'info_retention' : True,
                                  'inplace_option' : False,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'multirt',
                                  'labelctgy' : 'bnry'}})
    process_dict.update({'lbsm' : {'dualprocess' : self._process_smth,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_smth,
                                  'inverseprocess' : self._inverseprocess_smth,
                                  'info_retention' : True,
                                  'inplace_option' : False,
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'exclude',
                                  'labelctgy' : 'lbsm'}})
    process_dict.update({'lbfs' : {'dualprocess' : self._process_smth,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_smth,
                                  'inverseprocess' : self._inverseprocess_smth,
                                  'info_retention' : True,
                                  'inplace_option' : False,
                                  'defaultparams' : {'LSfit' : True},
                                  'NArowtype' : 'justNaN',
                                  'MLinfilltype' : 'exclude',
                                  'labelctgy' : 'lbfs'}})
    process_dict.update({'lbda' : {'dualprocess' : None,
                                  'singleprocess' : None,
                                  'postprocess' : None,
                                  'inplace_option' : False,
                                  'NArowtype' : 'datetime',
                                  'MLinfilltype' : 'exclude',
                                  'labelctgy' : 'mdsn'}})
    process_dict.update({'lgnr' : {'dualprocess' : self._process_absl,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_absl,
                                  'inverseprocess' : self._inverseprocess_absl,
                                  'info_retention' : False,
                                  'inplace_option' : True,
                                  'NArowtype' : 'nonzeronumeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'qbt5'}})
    process_dict.update({'lgn2' : {'dualprocess' : self._process_logn,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_logn,
                                  'inverseprocess' : self._inverseprocess_logn,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'NArowtype' : 'positivenumeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'qbt5'}})
    process_dict.update({'qbt5' : {'dualprocess' : None,
                                  'singleprocess' : self._process_qbt1,
                                  'postprocess' : None,
                                  'inverseprocess' : self._inverseprocess_qbt1,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'defaultparams' : {'integer_bits' : 4,
                                                     'fractional_bits' : 3,
                                                     'sign_bit' : True},
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'exclude',
                                  'labelctgy' : 'qbt5'}})
    process_dict.update({'sgn3' : {'dualprocess' : None,
                                  'singleprocess' : self._process_copy,
                                  'postprocess' : None,
                                  'inverseprocess' : self._inverseprocess_excl,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'defaultparams' : {'suffix' : ''},
                                  'NArowtype' : 'exclude',
                                  'MLinfilltype' : 'exclude',
                                  'labelctgy' : 'sgn2'}})
    process_dict.update({'sgn4' : {'dualprocess' : None,
                                  'singleprocess' : self._process_copy,
                                  'postprocess' : None,
                                  'inverseprocess' : self._inverseprocess_excl,
                                  'info_retention' : True,
                                  'inplace_option' : True,
                                  'defaultparams' : {'suffix' : ''},
                                  'NArowtype' : 'exclude',
                                  'MLinfilltype' : 'exclude',
                                  'labelctgy' : 'sgn2'}})
    process_dict.update({'sgn1' : {'dualprocess' : self._process_mltp,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_mltp,
                                  'inverseprocess' : self._inverseprocess_mltp,
                                  'info_retention' : False,
                                  'inplace_option' : True,
                                  'defaultparams' : {'multiply' : -1},
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'numeric',
                                  'labelctgy' : 'sgn2'}})
    process_dict.update({'sgn2' : {'dualprocess' : self._process_bkt3,
                                  'singleprocess' : None,
                                  'postprocess' : self._postprocess_bkt3,
                                  'inverseprocess' : self._inverseprocess_bkt3,
                                  'info_retention' : False,
                                  'inplace_option' : True,
                                  'defaultparams' : {'buckets' : [0]},
                                  'NArowtype' : 'numeric',
                                  'MLinfilltype' : 'singlct',
                                  'labelctgy' : 'sgn2'}})

    return process_dict
```