public class BinarySearch {
    //using recursive method
    public int binarySearchByRecursive(int array[],int x,int low,int high){
        if(high >= low){
            int mid = (high + low) / 2;

            if(array[mid] == x)
              return mid;

            if(array[mid] > x)
              return binarySearchByRecursive(array, x, low, mid -1);
            
            return binarySearchByRecursive(array, x, mid + 1, high);
        }
        return -1;
    }

    int binarySearchByIteration(int array[], int x,int low , int high){
        //repeat untill pointer low and high meet each other
        while(low <= high){
            int mid = (high + low) / 2;

            if(array[mid] == x)
              return mid;
            else if(array[mid] < x)   //moves to the right
              low = mid + 1;
            else
             high = mid - 1;
        }
        return -1;
    }
    public static void main(String[] args) {
        BinarySearch binarySearch = new BinarySearch();
        int array[] = {3,4,5,6,7,8,9,10};
        int arraySize = array.length;

        int elementSearched = 5;
        int result = binarySearch.binarySearchByIteration(array, elementSearched, 0, arraySize - 1);

        if(result == -1)
          System.out.println("Not found");
        else
          System.out.println("Element found at index "+result);
    }
}
