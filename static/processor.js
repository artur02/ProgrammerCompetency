var processor = (function () {

    $(function(){
        $("tr.group-item > td:not(tr.group-item>td:first-of-type)")
            .hover(
                function(){
                    $this = $( this );
                    $this.addClass("mover");
                    $this.prevUntil("td:first-of-type").addClass("mprev");

                },
                function(){
                    $this = $( this );
                    $this.removeClass("mover");
                    $this.prevUntil("td:first-of-type").removeClass("mprev");
                })
            .click(
                function(){

                    $this = $( this );
                    $this.siblings().removeClass("selected")
                    $this.siblings().removeClass("selectedPrev")

                    $this.prevUntil("td:first-of-type").addClass("selectedPrev");
                    $this.addClass("selected");
                });
    });

    var exp = function() {
        var ids = [];
        $("td.selected").each(function(){ ids.push($(this).data("id")) })
        return ids;
    };

    var imp = function(ids) {
        $("tr.group-item > td").removeClass("selected selectedPrev mover mprev");

        $(ids).each(function(){


            $("tr.group-item > td[data-id=" + this +"]").click();
        });
    };

    return {
        exp: exp,
        imp: imp
    }
})();