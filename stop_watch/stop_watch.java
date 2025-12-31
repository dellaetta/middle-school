class Main {
  public static void main(String[] args) throws InterruptedException {
    int timer;
    for(timer = 0; timer <= 10; timer++){
      System.out.println(timer);
      Thread.sleep(1000);
    }
  }
}
// make the timer not so fast when printed

