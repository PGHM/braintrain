//
//  Copyright © 2022 Jussi Päivinen. All rights reserved.
//

import Foundation
import SwiftUI

struct Teaser: Decodable {
    enum ImageType: String, Decodable {
        case rectangle
        case roundedRectangle
        case circle
    }

    let imageType: ImageType
    private let imageURL: URL

    let title: String
    let ingress: String?
    let category: String
    let paywalled: Bool
    let date: Date

    var image: Image {
        return Image(
            uiImage: UIImage(
                data: try! Data(contentsOf: imageURL)
            )!
        )
    }
}

// MARK: - Identifiable
extension Teaser: Identifiable {
    var id: String { title }
}
