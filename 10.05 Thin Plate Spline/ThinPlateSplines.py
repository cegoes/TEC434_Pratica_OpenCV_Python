import cv2
import numpy as np
from pathlib import Path

caminhoImagem = Path('10.05 Thin Plate Spline/len_std.png')

if __name__ == "__main__":

    img = cv2.imread(str(caminhoImagem))

    tps = cv2.createThinPlateSplineShapeTransformer()
    rows, cols, _ = img.shape

    sourcePoints = np.array([[0,0],
                            [0.5*cols, 0],
                            [cols, 0],
                            [cols, 0.5*rows],
                            [cols, rows],
                            [0.5*cols, rows],
                            [0, rows],
                            [0, 0.5*rows/2]],
                            np.float32)
    targetPoints = np.array([[0,0],
                            [0.5*cols, 0.25*rows],
                            [cols, 0],
                            [0.75*cols, 0.5*rows],
                            [cols, rows],
                            [0.5*cols, 0.75*rows],
                            [0, rows],
                            [0.25*cols, 0.5*rows]],
                            np.float32)
    
    sourcePoints=sourcePoints.reshape(-1,len(sourcePoints),2)
    targetPoints=targetPoints.reshape(-1,len(targetPoints),2)

    matches = list()

    for i in range(0,len(sourcePoints[0])):
        matches.append(cv2.DMatch(i,i,0))

    tps.estimateTransformation(targetPoints, sourcePoints, matches)

    out_img = tps.warpImage(img)

    cv2.imshow("Original", img)
    cv2.imshow("Distorcao", out_img)

    cv2.waitKey(0)

"""
# Código em C++
int main()
{

    cv::Mat img = cv::imread("C:/data/StackOverflow/Lenna.png");

    auto tps = cv::createThinPlateSplineShapeTransformer();
    std::vector<cv::Point2f> sourcePoints, targetPoints;
    sourcePoints.push_back(cv::Point2f(0, 0));
    targetPoints.push_back(cv::Point2f(0, 0));
    sourcePoints.push_back(cv::Point2f(0.5*img.cols, 0));
    targetPoints.push_back(cv::Point2f(0.5*img.cols, 0.25*img.rows));
    sourcePoints.push_back(cv::Point2f(img.cols, 0));
    targetPoints.push_back(cv::Point2f(img.cols, 0));
    sourcePoints.push_back(cv::Point2f(img.cols, 0.5*img.rows));
    targetPoints.push_back(cv::Point2f(0.75*img.cols, 0.5*img.rows));
    sourcePoints.push_back(cv::Point2f(img.cols, img.rows));
    targetPoints.push_back(cv::Point2f(img.cols, img.rows));
    sourcePoints.push_back(cv::Point2f(0.5*img.cols, img.rows));
    targetPoints.push_back(cv::Point2f(0.5*img.cols, 0.75*img.rows));
    sourcePoints.push_back(cv::Point2f(0, img.rows));
    targetPoints.push_back(cv::Point2f(0, img.rows));
    sourcePoints.push_back(cv::Point2f(0, 0.5*img.rows/2)); // accidentally unwanted y value here by 0.5 and /2
    targetPoints.push_back(cv::Point2f(0.25*img.cols, 0.5*img.rows));

    std::vector<cv::DMatch> matches;
    for (unsigned int i = 0; i < sourcePoints.size(); i++)
        matches.push_back(cv::DMatch(i, i, 0));

    tps->estimateTransformation(targetPoints, sourcePoints, matches); // this gives right warping from source to target, but wront point transformation
    //tps->estimateTransformation(sourcePoints, targetPoints, matches); // this gives wrong warping but right point transformation from source to target
    std::vector<cv::Point2f> transPoints;
    tps->applyTransformation(sourcePoints, transPoints);

    std::cout << "sourcePoints = " << std::endl << " " << sourcePoints << std::endl << std::endl;
    std::cout << "targetPoints = " << std::endl << " " << targetPoints << std::endl << std::endl;
    std::cout << "transPos = " << std::endl << " " << transPoints << std::endl << std::endl;

    cv::Mat dst;
    tps->warpImage(img, dst);

    cv::imshow("dst", dst);
    cv::waitKey(0);
};
"""