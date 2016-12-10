/**
 * Created by jorik on 10-12-2016.
 */
var Collision = {

    OverlapsWith: function(x1, y1, w1, h1, x2, y2, w2, h2) {
        return (
            (x1 + w1 > x2)
            && (x1 < x2 + w2)
            && (y1 + h1 > y2)
            && (y1 < y2 + h2)
        );
    }
};