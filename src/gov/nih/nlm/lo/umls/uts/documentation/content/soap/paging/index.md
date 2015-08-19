title=Paging
date=2015-08-19
updated=2015-08-19
type=page
status=unpublished
category=Paging, sorting, Filtering
navorder=1
~~~~~~



The Paging, Sorting, and Filtering (PSF) object of the UTS API 2.0 allows you to customize the results of your Web service calls in a variety of ways. The PSF object allows a great deal of flexibility in customizing your view of returned data.
 You can:

-   include or exclude criteria such as source vocabularies, language, term types, and others
-   sort your results by different fields, depending on the return type
-   choose the number of results displayed per page
-   choose number of pages of results returned

You can pass PSF objects as parameters on methods related to the UtsWsContentController and UtsWsFinderController objects.
*You must specify in your code the type of PSF object you are creating, since it exists under both the Metathesaurus Content and Finder packages.*

You can create the objects as follows:

~~~~
//your package names may differ depending on how you parsed the installation WSDLs.
//create a PSF object to be used in conjunction with UtsWsContentController objects
 UtsMetathesaurusContent.Psf psfMetaContent = new UtsMetathesaurusContent.Psf();
 
//create a PSF object to be used in conjunction with UtsWsFinderController objects
 UtsMetathesaurusFinder.Psf psfMetaFinder = new UtsMetathesaurusFinder.Psf();
~~~~
>

All the methods below are called on the hypothetical psfMetaContent object created in the code sample above.

>

**Method: **setPageLn( int )


#### Sample Input (Java):

~~~~
//this limits the number of results displayed per page to 10

 psfMetaContent.setPageLn(10);
~~~~
>

**Method: **setPageNum( int )


#### Sample Input (Java):

~~~~
psfMetaContent.setPageNum(2);
~~~~

