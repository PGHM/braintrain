//
//  Copyright © 2022 Jussi Päivinen. All rights reserved.
//

import SwiftUI

struct TeaserView: View {

    let teaser: Teaser

    let dateFormatter: DateFormatter = {
        let dateFormatter = DateFormatter()
        dateFormatter.dateFormat = "dd.MM.yyyy. hh:mm"
        return dateFormatter
    }()

    var body: some View {
        VStack(alignment: .leading, spacing: 10) {
            teaser.image
                .resizable()
                .applyTeaserImageShape(imageType: teaser.imageType)
                .scaledToFit()
                .frame(maxWidth: .infinity)
            Group {
                Text(teaser.title)
                    .font(.title)
                if let ingress = teaser.ingress {
                    Text(ingress)
                        .font(.subheadline)
                }
                HStack {
                    if teaser.paywalled {
                        StarView()
                            .frame(width: 25)
                    }
                    Text(teaser.category)
                        .font(.system(size: 20))
                    Text(dateFormatter.string(from: teaser.date))
                        .lineLimit(1)
                        .font(.system(size: 20))
                        .truncationMode(.tail)
                }
            }
        }
        .padding()
    }
}

struct TeaserView_Previews: PreviewProvider {
    static var previews: some View {
        Group {
            TeaserView(teaser: TeaserProvider.frontPageTeasers[0])
                .previewLayout(.sizeThatFits)
            TeaserView(teaser: TeaserProvider.frontPageTeasers[1])
                .previewLayout(.sizeThatFits)
            TeaserView(teaser: TeaserProvider.frontPageTeasers[2])
                .previewLayout(.sizeThatFits)
        }
    }
}

// I would have liked to do helper function like this:

//    @ViewBuilder private var teaserImageShape: some Shape {
//        switch teaser.imageType {
//            case .rectangle:
//                Rectangle()
//            case .roundedRectangle:
//                RoundedRectangle(cornerRadius: 50)
//            case .circle:
//                Circle()
//        }
//    }

// But an error occurs:
// Return type of property 'teaserImageShape' requires that '_ConditionalContent<_ConditionalContent<Rectangle, RoundedRectangle>, Circle>' conform to 'Shape'
// And the to solve that you'd have to type erasure Shape with something like AnyShape and not use @ViewBuilder or make @ShapeBuilder or something, sigh

private extension Image {
    @ViewBuilder func applyTeaserImageShape(imageType: Teaser.ImageType) -> some View {
        switch imageType {
            case .rectangle:
                clipShape(Rectangle())
            case .roundedRectangle:
                clipShape(RoundedRectangle(cornerRadius: 50))
            case .circle:
                clipShape(Circle())
        }
    }
}
