from product.repositories import get_last_six_review_per_user, get_user_review_count
from product.serializers import ReviewerStatSerializer


def get_current_user_statistic(user_id):
    review_list = get_last_six_review_per_user(user_id)
    reviews_count = get_user_review_count(user_id)
    review = ReviewerStatSerializer(review_list, many=True)
    return {"review_count": reviews_count, "review_list": review.data}
