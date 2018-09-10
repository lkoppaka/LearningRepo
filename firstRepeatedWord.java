package WordSearch;

import java.util.ArrayList;
import java.util.List;
//import org.apache.commons.lang.StringUtils;

/**
 * @author Lavanya
 *
 */
public class WordSearch{

	//returns the first repeated word in a given sentence based on the delimiter list
	//delimiter list is space, tab, comma (,), colon (:), semicolon (;), dash (-), and period (.)

	// 1. check for null sentence or string with no delimiters
	// 2. break sentence into words based on the delimiter list provided as regex
	// 3. start inserting the words into an arraylist in order.
	// 4. if a word existing in the list occurs again, break the loop
	// 5. return the word else return "No repeated word"

	//@param: String - Takes the sentence in which the first repeated word needs to be found
	//@return: String - the first repeated word in the sentence other than empty strings
	 
	protected String firstRepeatedWord(String sentence)
	{
	    
	    if(sentence == null || sentence.length() <= 0)
	        return "none found";
	        //throw new Exception("Empty sentence received!! Aborting");
	    
	    //delimiter list is space, tab, comma (,), colon (:), semicolon (;), dash (-), and period (.).
	    String[] wordsInSentence = sentence.split("[ \\t,:;\\-.]"); //delimiter list needs to be externalized for future changes
	    List<String> wordList = new ArrayList<String>(wordsInSentence.length);
	    
	    // traverse again from first word to find the first repeated word
	    for(String s: wordsInSentence){
	        //only insert into the word-list if it is not an empty string
	        if(s!= null && s.trim().length() > 0){ 
	            if(!wordList.contains(s))
	                wordList.add(s);
	            else {
	                return s;
	            }
	        }
	    }
	    return "none found";
	}
	
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		WordSearch test = new WordSearch();
		String returnValue = test.firstRepeatedWord("This has a test that has test");
		System.out.println("Return:: " + returnValue);
	}

}
