class Slider {
  constructor() {
    this.getId(); //will get and add ids to array
    this.changeSlide(); //will change slide
  }
  imageId = []; //image id arrary variablle

  getId() {
    // change ".slides" className  ->in html of parent div and here too and it will
    //work flowlessly no other change required for js code to work
    //" ID's" should be different of child of ".slide" class to work
    const slideNode = document.querySelector(".slides").childNodes;
    // console.log(slideNode);
    slideNode.forEach(el => {
      if (el.id) {
        // console.log("->", el.id);//print image slide id
        this.imageId.push(el.id); //will add slide ids to array
      }
    });
  }
  async changeSlide() {
    // console.log(i);
    // console.log("called ");

    for (let i = 0; i < this.imageId.length; i++) {
      document.querySelector("#" + this.imageId[i]).className +=
        " active";

      // console.log(this.imageId);
      await this.slideTimer(3500); //sync function act as timer/sleep fn
    }
    this.removeClassName(); //will call remove fn over and over
  }
  removeClassName() {
    for (let i = 0; i < this.imageId.length; i++) {
      let active = (document.querySelector(
        "#" + this.imageId[i]
      ).className = " img ");
    }
    this.changeSlide(); //call slide function over and over
  }
  // sleep function
  slideTimer(ms) {
    return new Promise(resolve => {
      setTimeout(resolve, ms);
    });
  }
}

// calling class/starter
new Slider();
