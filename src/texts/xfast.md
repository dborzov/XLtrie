Predecessor search for Big Data: x-fast tries, locality of reference and all that
==============================

### *Abstract:* We get a bird eye view on the fascinating field of the locality of reference-type of problems and then get practical and solve our toy problem by implementing an x-fast trie in Python.

Imagine you are developing a flight search website. You need to build a tailored search index that is really good at one task: for the given date and search criteria returns the list of the next flights. How is it better to approach designing this?

This is an example of encountering predecessor/successor search problem in practice. Predecessor/successor search (or predecessor search for 'short') stands for cases when we have some dictionary (*in our case, the flight timetable*) with its keys (*departure times*) making up a subset of some ordered sequence (*like all minutes in the time range of interest or something*).

We want to design a system that for a given query element of that sequence (such as *our preferable flying date and time*) would return the closest next subsequest element that is a key of our dictionary(*next flight from our query time*):

\[
![Img](./img/arrow.png)
\]



For the flight search website that would include the two following typical database tasks:

* **Looking up**: searching for the next closest flights meeting some criteria for the given date and time (like *"the next flight to Paris on Oct 9th after 9am"*);
* **Updating**: adding, editing or deleting specific flight records on request (like *"the flight to Paris on Oct 9th 10am is canceled"*).

This problem of optimizing the flight is an example of the predecessor/successor search problem. It involves storing a dictionary with keys that make a subset of some subset

 X-fast tries is a data structure designed to store a subset of elements from a sequence in such a way so that it is possible to retrieve the next closest  element easily. People refer to such problems as the predecessor/ successor search.

I have been reading up about [x-fast tries](http://en.wikipedia.org/wiki/X-fast_trie) recently and decided to write up some notes  and also to make a simple python implementation to go along with it.


Obviously, it is incredibly inefficient to just store them as a list and go through the list each time. We need some kind of a search tree.

Times of planes leaving (for example, in minutes) make up a subset of all the possible times (all minutes in the span of the existence of that specific airport). thus we can store them as a set of natural numbers  in a certain range of integers.

So with that representation we can use the Direct Access Table. That is, make up a binary table of size  |S|.

What are some ways to tackle the predecessor/successor problem? Naively we can just move along up the Direct Access Table until we stumble upon the next record. The worst case scenario here would be just going through the whole empty table, **O(m)** .

One improvement is to store pointers for predecessor/successor elements at each element. It does improve the predecessor/successor retrieval to just **O(1)** . However, we have a inserting or deleting elements becomes a costly procedure as we have to reassign every nearby value, **O(m)**.

Here is the proposition. We build an ordered binary tree atop the m elements and mark every node that is a parent of the checked element. With each layer having two times less elements we only increased the total size of the array by two.

## Toy problem
Here is a nice toy problem that I came up with in hope that it would make some cool-loking plots.

With movie and tv show titles such as X-files, X-men and American History X, we have a trope of X standing for anything misterious (and heavily implied to be hip). How often are movies with such titles released? What was the first X-movie released since your birth?

To find out, let us build the X-fast trie index for such X-titled movies by the year of release.

Here is a plot of what we get:

\[
![Img](./img/movies.png)
\]

Pretty nice, huh?
