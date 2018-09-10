package WordSearch;

import org.junit.Assert;
import org.junit.Test;

import WordSearch.WordSearch;

public class WordSearchJunit {
	
	WordSearch myTestClass;
	
	public WordSearchJunit(){
		if(myTestClass == null)
			myTestClass = new WordSearch();
	}
	
	@Test
	public void testNullSentence() {
		String returnValue = myTestClass.firstRepeatedWord(null);
		Assert.assertEquals("Return value should be none found", returnValue, "none found");
	}
	
	@Test
	public void testEmptySentence() {
		String returnValue = myTestClass.firstRepeatedWord("    ");
		Assert.assertEquals("Return value should be none found", returnValue, "none found");
	}
	
	@Test
	public void testDelimitersInSentence() {
		String returnValue = myTestClass.firstRepeatedWord("I had;::had a great dream");
		Assert.assertEquals("Return value should be had", returnValue, "had");
	}
	
	@Test
	public void testCaseInSentence() {
		String returnValue = myTestClass.firstRepeatedWord("I had;::Had a great dream");
		Assert.assertEquals("Return value should be none found", returnValue, "none found");
	}
	
	@Test
	public void testSubstringInSentence() {
		String returnValue = myTestClass.firstRepeatedWord("I put:my:putter in the bag;");
		Assert.assertEquals("Return value should be none found", returnValue, "none found");
	}
	
	@Test
	public void testMultipleDuplicatesInSentence() {
		String returnValue = myTestClass.firstRepeatedWord("This has a test that has test");
		Assert.assertEquals("Return value should be has", returnValue, "has");
	}

}
