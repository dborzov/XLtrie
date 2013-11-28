Predecessor search for Big Data: intro to x-fast tries
==============================

### *Abstract:* Abstracticus


Imagine you are developing a flight search engine and need to make the search lookup time as fast as possible. You know that the How should you organize your flight indexing to speed up the search?

####

Imagine you are developing an internet flight search service. You want to design some kind of indexing in such a way so that they would be effective at processing queries you expect to be most common in your applications.

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
