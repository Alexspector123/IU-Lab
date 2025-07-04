package Question5;

import java.util.HashMap;
import java.util.List;

class Result {

    /*
     * Complete the 'checkMagazine' function below.
     *
     * The function accepts following parameters:
     *  1. STRING_ARRAY magazine
     *  2. STRING_ARRAY note
     */

    public static void checkMagazine(List<String> magazine, List<String> note) {
    // Write your code here
    if(magazine.size() < note.size()){
        System.out.println("No");
    }
    else{
        boolean check = true;
        HashMap<String, Integer> list = new HashMap<String, Integer>();
        for(String maga : magazine){
            if(list.containsKey(maga) == false){
                list.put(maga,1);
            }
            else
            {
                list.replace(maga, list.get(maga)+1);
            }
        }
        for(String word : note){
            if(list.containsKey(word) == false){
                check = false;
                break;
            }
            else{
                if(list.get(word) == 0) {
                    check = false;
                    break;
                }
                list.replace(word, list.get(word)-1);
            }
        }
        if(check == true){
            System.out.println("Yes");
        }
        else{
            System.out.println("No");
        }
    }
    }

}